a = []
a.append('s#......#...#..')
a.append('.#.#...#..#...#')
a.append('.#.#...##..#.##')
a.append('.#.#...##..#..#')
a.append('.#.#....##.##.#')
a.append('.#.#....#..#..#')
a.append('.#.#....#..#..#')
a.append('...#....#..#..#')
a.append('...#.......#..e')

b = a.copy()
m = len(a)
n = len(a[0])
start = []
end = []

for i in range(m):
    for j in range(n):
        if a[i][j] == 's':start = [i,j]
        if a[i][j] == 'e':end = [i,j]

gone = set(tuple(start))
now = [[start,[]]]

def res(action):
    i,j = start
    for x in action:
        i += x[0]
        j += x[1]
        b[i] = list(b[i])
        b[i][j] = 'o'
        b[i] = ''.join(b[i])


while now:
    do = now.pop(0)
    i,j = do[0]
    road = do[1]
    for x in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        if tuple(x) not in gone and min(x[0],x[1]) >= 0 and x[0] <= m-1 and x[1] <= n-1:
            pos = [x[0],x[1]]
            action = [[x[0]-i,x[1]-j]]
            if a[x[0]][x[1]] == 'e':
                res(road)
                for y in b:
                    print(y)
                exit()
            if a[x[0]][x[1]] == '.':
                now.append([pos,road+action])
                gone.add((x[0],x[1]))

print(-1)