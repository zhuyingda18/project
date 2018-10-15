import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

n,k,q = LI()
a = LI()

po = {}

for i in range(n):
    if a[i] in po:po[a[i]].append(i)
    else:po[a[i]] = [i]

def comb(a,b):
    c = []
    d = []
    for x in a:
        c.append([x,0])
    for x in b:
        c.append([x,1])
    c.sort()
    op1 = 0
    op2 = 0
    do = 0
    l = 0
    for x in c:
        if x[1] == 0:op1 = 1 - op1
        if x[1] == 1:op2 = 1 - op2
        if op1+op2 >= 1:
            d.append(x[0])
            do = 1
        elif do == 1:
            d.append(x[0])
            do = 0
    return(d)

def count(a):
    res = 0
    for i in range(len(a)//2):
        p = a[i]
        q = a[i+1]
        if p<0:p = 0
        if p<0:q=0
        if q>=n:q = n-1
        res += q-p+1
    return(res)


a_ = sorted(a)
a1 = sorted(list(set(a)))
do = n-k+1
min0 = a_[q-1]-a_[0]
nopa = []


for x in a1:
    nopax = [-q-2]
    end = -q-1
    k = len(po[x])
    for i in range(k):
        temp = sorted(po[x])
        if temp[i]-q > end:
            nopax.append(end)
            nopax.append(temp[i]-q+1)
        end = temp[i]+q-1
    nopax.append(end)
    nopa = comb(nopa,nopax)
    if count(nopa) > k-1:
        break
    print(nopa)
    min0 = min(min0,a_[q-1+k]-a_[k])


print(min0)













