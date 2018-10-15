h,w = list(map(int, input().split()))
data = {}
mod = {0:0,1:0,2:0,3:0}
for i in range(h):
    temp = input()
    for x in temp:
        if x in data:data[x]+=1
        else:data[x] = 1
for x in data.values():
    temp = x%4
    mod[temp] += temp

if mod[1] == 1 and mod[3] == 0 and h%2 == 1 and w%2 == 1 and mod[2]<= h+w-2 and (h+w-2-mod[2])%4==0:print('Yes')
elif mod[1] == 0 and mod[3] == 1 and h%2 == 1 and w%2 == 1 and mod[2]<= h+w-4 and (h+w-4-mod[2])%4==0:print('Yes')
elif mod[1] == 0 and mod[3] == 0 and h%2 == 1 and w%2 == 0 and mod[2]<= w     and (w-mod[2])%2==0    :print('Yes')
elif mod[1] == 0 and mod[3] == 0 and h%2 == 0 and w%2 == 1 and mod[2]<= h     and (h-mod[2])%2==0    :print('Yes')
elif mod[1] == 0 and mod[3] == 0 and h%2 == 0 and w%2 == 0 and mod[2]==0:print('Yes')
else: print('No')
