arr = [1, 2, 8, 10, 11, 12, 19]
x = 5
if x<arr[0]:print(arr[0])
elif x>arr[len(arr)-1]:print(-1)
left = 0
right = len(arr)-1
while left<=right:
    mid = (left+right)//2
    if arr[mid] >= x:
        answer  = mid
        right = mid-1
    else:
        left = mid+1
print(mid)        
