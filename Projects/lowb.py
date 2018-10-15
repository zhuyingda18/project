def lowbit(x):
    return x&(-x)

a = [1,2,3,4,5,6,7,8,9]
print(a)
for i in range(len(a)):
    a[i] = lowbit(a[i])
print(a)