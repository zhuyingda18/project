n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    a[i] -= (i+1)
a.sort()
res = 0
for i in range(n//2):
    res += a[-i-1]-a[i]
print(res)
