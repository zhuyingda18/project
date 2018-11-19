a = 'ababdababcc'
num = 1 #输出前几个结果
# 添加，删除，替换
# 分成两部分后，添加和删除的意义相同，只考虑删除

res = []
n = len(a)

for i in range(2*n+1): # 把字符串分成两部分
    left = a[:i//2]
    right = a[(i+1)//2:]
    rev = 0
    omi = a[i//2:(i+1)//2]
    if len(right) < len(left):
        left,right = right,left # left为短串，right为长串
        rev = 1
    right = right[::-1]
    l = len(left)
    r = len(right)
    # 把长串每个字母与短串的每个位置做对应，求出此时的cost
    # 有字符处只能插入一个，无字符处无限制
    # 初始化dp , 插入这个位置时，到这个位置为止的cost以及分配方法
    dp = [[0,0] for i in range(2*l+1)]
    # 初始化cost , 到这个位置为止(包含)，最小的cost以及分配方法
    cost = [[i//2] for i in range(2*l+1)]   # [1,1,1,1,2,2,3,3...]
    # 进行dp
    for i in range(r):
        tar = right[i]
        for j in range(2*l+1):  # dp更新
            if j%2 == 0:#插入在空位,加上包含空位的cost + 删除
                dp[j][0] = cost[j][0] + 1
                dp[j][1] = cost[j][1:].copy()   # 存路径
            if j%2 == 1:#插入在字符位
                dp[j][0] = cost[j-1][0]
                dp[j][1] = cost[j-1][1:].copy()  # 存路径
                if tar != left[j//2]: dp[j][0] += 1  # 字符不相同，需要换
        po = 0 # 插入位初始化
        cost[0][0] += 1
        cost[0].append(0)
        mincost = cost[0][0]
        for j in range(1,2*l+1):  # cost更新
            # realcost 需要加上最后对应位之后的需要删除的字符数
            realcost = cost[j-1][0] + ((j+1) //2 - (cost[j-1][-1]+1)//2)     # 插在前面的cost,每次更新，如果j是字符，计算其cost
            dpcost = dp[j][0]             # 插在这一位的cost
            if dpcost < realcost:
                cost[j] = [dpcost] + dp[j][1].copy() + [j]
            else:
                cost[j] = cost[j-1].copy()
                cost[j][0] = realcost
    x = cost[-1]
    count = 0
    for y in x[1:]:
        if y%2 == 1: count += 1
    res.append([x[0],count+len(omi),x[1:].copy(),left,right,rev,omi]) # cost,长度，操作，左半，右边，是否交换，中间
res.sort(key = lambda x:(x[0],x[1]))

print('*为删除,_为不变')

for output in res[:num]:
    act = output[2]
    outleft = output[3]
    outright = output[4]
    rev =output[5]
    outmid = output[6]
    actleft = []
    actright = []
    if outmid:actmid = '_'
    else:actmid = ''

    for i in range(len(act)):   # 输出right,action
        if act[i] % 2 == 0:actright.append('*')
        else:
            if outright[i] == outleft[act[i]//2]:actright.append('_')
            else:actright.append(outleft[act[i]//2])
    for i in range(len(outleft)):  # 输出left,action
        if 2*i+1 in act:actleft.append('_')
        else:actleft.append('*')
    actright = ''.join(actright)
    actleft = ''.join(actleft)
    if rev:
        outleft,outright = outright,outleft
        actleft,actright = actright,actleft
        actright = actright[::-1]
        actleft = actleft[::-1]
    outright = outright[::-1]
    actright = actright[::-1]
    action = actleft+actmid+actright
    print('cost =',output[0])
    print('原本',a)
    print('操作',action)
    changed = []
    for i in range(len(a)):
        x = action[i]
        if x == '_':changed.append(a[i])
        elif x != '*':changed.append(x)
    print('结果',''.join(changed))







