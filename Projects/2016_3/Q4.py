n = int(input())
pare = input()
plan = []
weight = list(map(int,input().split(' ')))

left = 0
right = 0
w_min = weight[0]
w_id  = 0
weightsum = 0

for i in range(n):
    plan.append([0,0])
    if weight[i] < w_min:w_id = i
    if pare[i] == '(':left+=1
    if pare[i] == ')':right+=1
    if right > left:
        left +=1
        plan[w_id][0] += 1
        weightsum += weight[w_id]

plan.append([0,0])
w_min = weight[-1]
w_id = n

left = 0
right = 0

for i in range(0,n)[::-1]:
    if weight[i+1] < w_min: w_id = i+1
    left += plan[i+1][0]
    if pare[i] == '(': left += 1
    if right < left:
        plan[w_id][1] += left - right
        weightsum += weight[w_id]*(left - right)
        right = left
    if pare[i] == ')': right += 1

print(weightsum,plan)

