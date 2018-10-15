a = [1,2,3]

def push(now,a):
    rest = set(a) - set(now)
    for x in rest:
        now.append(x)
        if len(now) == len(a):
            res.append(now.copy())
        else:push(now,a)
        now.pop(-1)

res = []
push([],a)
print(res)