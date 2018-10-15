s1 = list(input())
s2 = list(input())
can = 0
start = ord('a')
end = ord('z')
res = []

for i in range(start,end+1):
    for j in range(start,end+1):
        s1c = s1.copy()
        s2c = s2.copy()
        for k in range(len(s1)):
            if s1c[k] == chr(i): s1c[k] = chr(j)
            if s2c[k] == chr(i): s2c[k] = chr(j)
        print(s1c,s2c)
        if s1c == s2c:
            can = 1
            res.append([chr(i),chr(j)])
print(can,res)