n,m,k = list(map(int, input().split()))
done = 0
for i in range(n+1):
    for j in range(m+1):
        r = i*(m-j)+j*(n-i)
        if r == k:
            print('Yes')
            done = 1
            break
    if done == 1:break
if done == 0:print('No')