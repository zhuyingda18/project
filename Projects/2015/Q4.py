import sys
from heapq import heappush, heappop

# sys.stdin = open('pro4_1.txt', 'r')
N = int(input())
data = []
for i in range(N):
    s, c = map(int, input().split())
    data.append((s, i, c))
data.sort()
print(data)
p = data[0][0]  # 起始时间
q = []
ans = [0 for _ in range(N)]

# [(2, 3, 4), (3, 0, 3), (4, 2, 2), (10, 1, 1)]
# 存入，开始时间，优先度，剩余时间

# 每次读取一个新任务， 如果到这个任务的开始时间为止还有空闲时间，那么可以处理任务列表里优先度较高的
# 所有任务读取完毕以后，然后按优先度处理剩余任务
for s, i, c in data:
    # 读取一个新任务（起始时间最早）
    if p < s:     # 如果现在时间还没到做任务的时间，那么可以先干别的事情
        while q:  # 考察堆里的任务
            j, d = heappop(q)    # 抽出来一个优先度最高的（
            if p + d <= s:       # 如果没有碰到这个区块，那么可以直接做这个任务
                p += d           # 现在时间直接加上任务时间
                ans[j] = p - 1   # 完成的时间为现在时间-1
            else:
                heappush(q, (j, d - (s - p)))   #如果超出了，这个任务还没完成，把它塞回去
                break
        p = s      # 更新时间
    heappush(q, (i, c))     #如果现在时间已经超过了做任务的时间，那么把它塞进任务列表


# 扫一遍以后如果q里还有任务，按照优先级开始做
while q:
    j, d = heappop(q)
    p += d
    ans[j] = p - 1
for a in ans:
    print(str(a))