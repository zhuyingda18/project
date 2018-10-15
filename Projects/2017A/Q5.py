n,m = list(map(int(),input().split(' ')))
# 向右 向左 n
A = input()
B = input()
# 向下 向上 m
C = input()
D = input()

C1 = []
D1 = []
CD1 = []
CD  = 0
c = 0
d = 0

sumver = 1
for i in range(m):
    if C[i] == 1:
        c +=1
    if D[i] == 1:
        d +=1
    if C[i] == 1 and D[i] == 1:    # [0 12345]
        CD += 1
    if C[i] == 1 or D[i] == 1:
        C1.append(c)
        D1.append(d)
        CD1.append(CD)
#  1<=j,k<=n 2**(CD1[k]-CD[j-1])

def side(C1,D1,A,n):
    a = 0
    for i in range(n):
        if A[i] == 1:a+=1
    # 剩下x-1,y, C(x+y-1,y)



