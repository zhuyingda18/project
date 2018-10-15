import sys
import copy
sys.setrecursionlimit(10000)  # set the maximum depth as 10000

f = open('A-large-practice.txt')
f1 = open('large_output.txt','w')
# f = open('A-small-practice.txt')
# f1 = open('small_output.txt','w')
task = int(f.readline())


def forward(save,last,num): #BFS
    global do,circle
    if do > 0:return()
    for x in dic[num]:
        if x != last and do == 0:
            if x in save:
                do = x
                circle.append(do)
                return(x)
            save.add(x)
            forward(save,num,x)

def dfs(num):
    global dic1,do,save
    if do > 0: return ()
    if dic1[num] == []:
        save.pop(-1)
        dfs(save[-1])
        return()
    next = dic1[num][0]
    if next in save:
        id = save.index(next)
        save = save[id:]
        do = 1
        return()
    dic1[num].remove(next)
    dic1[next].remove(num)
    save.append(next)
    dfs(next)


for i in range(task):
    n = int(f.readline())
    dic = {}
    save = set([1]) #forward
    save = [1]
    circle = []
    for j in range(n):dic[j+1] = []
    resdic = copy.deepcopy(dic)
    for j in range(n):
        readin = f.readline().split(' ')
        x = int(readin[0])
        y = int(readin[1])
        dic[x].append(y)
        dic[y].append(x)
    do = 0
    dic1 = copy.deepcopy(dic)
    # forward(save,0,1)
    dfs(1)
    nowgroup = set(save)
    nextgroup = set()
    count = 0
    while len(nowgroup) <= n:
        for x in nowgroup:
            if resdic[x] == []:resdic[x] = count
            nextgroup = nextgroup | set(dic[x])
        if len(nowgroup) == n:break
        # print(nowgroup,nextgroup,dic)
        nowgroup,nextgroup = nowgroup | nextgroup,nextgroup - nowgroup
        count += 1
    result = ''
    for j in range(n):
        result += ' ' + str(resdic[j+1])
    f1.write("Case #{}:{}\n".format(i+1,result))
    # f1.write('Case #%d:%s\n' %(i+1,result))



