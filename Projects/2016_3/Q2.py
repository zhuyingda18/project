import time
a,b,k = list(map(int,input().split(' ')))

st = time.time()
m = 0

a1 = 0
b1 = 0.5

count = 0

for i in range(k):
    a1 += a
    b1 += b
    m = min(a1,b1)
    if m == a1:
        b1 -= b
    else:
        a1 -= a

en = time.time()

if m == a1:
    print('a', a1)
else:
    print('b',b1)

print(en-st)
