a = list(input())
data = {}

n = len(a)

for x in a:
    if x in data:data[x]+=1
    else:data[x]=1

sorted(data,key= lambda x:x[0])
res = []
last = ''
do = 0
tar = ''
if max(data.values()) > n//2 + n%2:print(-1)    # 大于一半直接输出
else:
    for i in range(n):
        if do == 0:     # do = 1 说明剩下已经有数大于一半
            if (n-i)%2 == 1 and max(data.values()) == (n-i+1)/2:  # 这个只会运行一次
                for x in data.keys():    #找到最大value的key
                    if data[x] == (n-i+1)/2:
                        tar = x
                        do = 1
                        break
        if do == 1 and (n-i)%2 == 1: # do=1后，剩余数奇数情况直接输出
            last = tar
            res.append(tar)
            continue
        else:    # 没有快捷输出的情况 or 剩余数偶数个的情况，选个最小的输出
            for x in data.keys():
                if data[x]>0 and x !=last:
                    res.append(x)
                    last = x
                    data[x] -= 1
                    break
print(''.join(res))















#
# left = 0
# right = 2
#
# while right <= len(res)-1 and left <= len(res)-3:
#     if right == left+1:right+=1
#     if res[left] == res[left+1]:
#         while res[right] == res[left] and right<len(res)-1:
#             right+=1
#         res[left+1],res[right] = res[right],res[left+1]
#     left += 1
#
# print(''.join(res))
#
# right = len(res) - 1
# left  = len(res) - 3
#
# while left >= 0 and right >= 2:
#     print(left,right)
#     if right == left+1:left-=1
#     if res[right] == res[right-1]:
#         while res[right] ==res[left] and left >1:
#             left -=1
#         res[right-1],res[left] = res[left],res[right-1]
#     right -= 1
#
# print(''.join(res))
#
#
#
#
