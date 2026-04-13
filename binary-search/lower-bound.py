arr = [2, 3, 7, 10, 11, 11, 25]
target = 11
left = 0
right = len(arr)-1
answer = len(arr)

while left<=right:
    mid = (left+right)//2
    if arr[mid]==target:
        answer = mid
        right = mid-1
    else:
        left = mid+1
print(answer)        
            
                