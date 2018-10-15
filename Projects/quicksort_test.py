a = [1,3,5,7,9,2,4,6,8,10]

def quicksort(l,left,right):
    if left >= right:return()
    low = left
    high = right
    key = l[left]
    while left < right:
        while left < right and key < l[right]:right -= 1
        l[left] = l[right]
        while left < right and key >= l[left]:left += 1
        l[right] = l[left]
    l[left] = key
    quicksort(l,low,left-1)
    quicksort(l,right+1,high)

quicksort(a,0,len(a)-1)
print(a)