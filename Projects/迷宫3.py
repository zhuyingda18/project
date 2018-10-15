# 破坏墙有cost,最大破坏数,传送门

a = []
a.append('s.................###*........')
a.append('.########.........###########.')
a.append('........#.........###.........')
a.append('#######.#.........###.########')
a.append('........#.........###.........')
a.append('.########.........###########.')
a.append('........#.........###.........')
a.append('#######.#.........############')
a.append('......#.#.........###.........')
a.append('#####.#.#.........###########.')
a.append('...##.#.#........####.........')
a.append('...##.#.#........####.########')
a.append('*..##...#........####........e')



b = a.copy()
m = len(a)
n = len(a[0])
start = []
end = []


cost1 = 1       # 普通点
cost2 = 200      # 墙
cost3 = 5       # 传送
num = 10       # 最多敲几面
tran = []

for i in range(m):
    for j in range(n):
        if a[i][j] == 's':start = [i,j]
        if a[i][j] == 'e':end = [i,j]
        if a[i][j] == '*':tran.append([i,j])

gone = {tuple(start):0}
save = []
now = [[start,[],0,0]]    # 起始点，路径，费用，破坏数
now1 = []    # 墙
now2 = []   # 传送
count = 0

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
        if a[i][j] == '#':b[i][j] = 'x'
        if a[i][j] == '*': b[i][j] = 'T'
        b[i] = ''.join(b[i])

dic = {0:now,1:now1,2:now2}

while now or now1 or now2:
    count += 1
    do = []
    if now:do.append([now[0][2],0])
    if now1:do.append([now1[0][2],1])
    if now2:do.append([now2[0][2],2])
    do = dic[sorted(do)[0][1]].pop(0)
    save.append(do)
    i,j = do[0]
    road = do[1]
    p = do[2]
    des = do[3]
    for x in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        if tuple(x) in gone:
            if gone[tuple(x)] <= des:continue
        if min(x[0],x[1]) >= 0 and x[0] <= m-1 and x[1] <= n-1:
            pos = [x[0],x[1]]
            action = [[x[0]-i,x[1]-j]]
            if a[x[0]][x[1]] in ['.','*']:
                now.append([pos,road+action,p+cost1,des])
                gone[(x[0],x[1])] = des
            if a[x[0]][x[1]] == '#' and des < num:
                if tuple(x) in gone:
                    if gone[tuple(x)] <= des+1: continue
                now1.append([pos, road + action,p+cost2,des+1])
                gone[(x[0], x[1])] = des+1
            if a[x[0]][x[1]] == '*':
                for y in tran:
                    if y != [x[0],x[1]]:
                        action = [[y[0]-i,y[1]-j]]
                        now2.append([y,road+action,p+cost3,des])
                        gone[(y[0], y[1])] = des
            if a[x[0]][x[1]] == 'e':
                res(road)
                for y in b:
                    print(y)
                print('cost =',p+1)
                print(count)
                exit()

print(-1)

# output()
# for x in b:
#     print(x)