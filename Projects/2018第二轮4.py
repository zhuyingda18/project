a = [1,1,1,1,1,1,1,1,1]
n = len(a)
tree = [0]*n

def lowbit(x):
    return x&(-x)

def read(i):
    res = 0
    while i > 0:
        res += tree[i-1]
        i -= lowbit(i)
    return res

def build():
    for i in range(1,n+1):
        j = i
        while j <= n:
            tree[j-1] += a[i-1]
            j += lowbit(j)

def data(left,right):


def search(l,r):
    left = r
    right = r
    dp1_,dp2_,dp3_,dp4_ = 0,0,0,0
    while left <= l:
        if right - lowbit(right) >= l: left = right - lowbit(right)
        if right - 1 >= l: left = right -1
        dpdata = data(left,right)
        dp1 = max(dp1_+dpdata[0],dpdata[1])
        dp2 = max(dp2_,dp1,dp1_+dpdata[2],dpdata[3])
        dp3 = min(dp3_+dpdata[0],dpdata[4])
        dp4 = min(dp4_,dp3,dp3_+dpdata[5],dpdata[6])
        left -= 1
        right = left
        dp1_,dp2_,dp3_,dp4_ = dp1,dp2,dp3,dp4
    return max(dp2,-dp4)



build()
print(read(4))