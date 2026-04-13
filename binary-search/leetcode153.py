nums = [4, 5, 6, 7, 0, 1, 2]
left = 0
right = len(nums)-1
minimum = 5001
while left<=right:
    mid = (left+right)//2
    minimum = min(minimum,nums[mid])
    if nums[mid]>nums[left]:
        minimum = min(nums[left],minimum)
        left = mid+1
    else:
        right = mid-1
print(minimum)        
