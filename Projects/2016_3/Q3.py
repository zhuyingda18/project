import time


def dfs(dom,k):
    global res
    if k == n:
        t = simulation(dom)
        print(dom,t)
        res += t
    else:
        dom[que[k][0]][que[k][1]] = 'R'
        dfs(dom,k+1)
        dom[que[k][0]][que[k][1]] = 'C'
        dfs(dom,k+1)


def simulation(dom):
    time = 0
    sit = []
    for i in range(r): sit.append([0] * c)
    for i in range(r):
        for j in range(c):
            if sit[i][j] == 0:
                time +=1
                sit[i][j] = 1
                i1 = i
                j1 = j
                while 1:
                    if dom[i1][j1] == 'R' and j1<c-1:
                        if sit[i1][j1+1] == 0:
                            sit[i1][j1+1] = 1
                            j1 += 1
                            continue
                    if dom[i1][j1] == 'C' and i1<r-1:
                        if sit[i1+1][j1] == 0:
                            sit[i1+1][j1] = 1
                            i1 += 1
                            continue
                    break
    return(time)



r,c = list(map(int,input().split(' ')))
dom = []
que = []
res = 0
for i in range(r):
    dom.append(list(input()))

st = time.time()
for i in range(r):
    for j in range(c):
        if dom[i][j] == '?':
            que.append([i,j])

n = len(que)

dfs(dom,0)

ed = time.time()
print(res/(2**n))
print(ed-st)





