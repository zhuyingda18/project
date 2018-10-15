# 带权重

a = []
a.append('s#...####......')
a.append('.#.#.####.....#')
a.append('.#.#.####..#..#')
a.append('.#.#.####..#..#')
a.append('.#.#.####..#..#')
a.append('.#.#.####..#..#')
a.append('.#.#.####..#..#')
a.append('...#.####..#..#')
a.append('...#.###...#..e')

b = a.copy()
m = len(a)
n = len(a[0])
start = []
end = []


cost1 = 1
cost2 = 50

for i in range(m):
    for j in range(n):
        if a[i][j] == 's':start = [i,j]
        if a[i][j] == 'e':end = [i,j]

gone = set(tuple(start))
save = []
now = [[start,[],0]]
now1 = []

def output():
    for x in save:
        i = x[0][0]
        j = x[0][1]
        b[i] = list(b[i])
        b[i][j] = x[2]

def res(action):
    i,j = start
    for x in action:
        i += x[0]
        j += x[1]
        b[i] = list(b[i])
        if a[i][j] == '.':b[i][j] = 'o'
        else:b[i][j] = 'x'
        b[i] = ''.join(b[i])

while now or now1:
    if not now:do = now1.pop(0)
    elif not now1:do = now.pop(0)
    elif now[0][2] > now1[0][2]: do = now1.pop(0)
    else: do = now.pop(0)
    save.append(do)
    i,j = do[0]
    road = do[1]
    p = do[2]
    for x in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        if tuple(x) not in gone and min(x[0],x[1]) >= 0 and x[0] <= m-1 and x[1] <= n-1:
            pos = [x[0],x[1]]
            action = [[x[0]-i,x[1]-j]]
            if a[x[0]][x[1]] == '.':
                now.append([pos,road+action,p+cost1])
                gone.add((x[0],x[1]))
            if a[x[0]][x[1]] == '#' :
                now1.append([pos, road + action,p+cost2])
                gone.add((x[0], x[1]))
            if a[x[0]][x[1]] == 'e':
                res(road)
                for y in b:
                    print(y)
                exit()

