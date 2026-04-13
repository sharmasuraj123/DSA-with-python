nums = [1, 3, 5, 6]
target = 2
answer = len(nums)
left = 0
right = len(nums)-1
while left <= right:
    mid = (left+right)//2
    if nums[mid]==target:
        answer = mid
    elif nums[mid]<target:
        answer = mid+1
        left = mid+1
    else:right = mid-1
print(answer)    
