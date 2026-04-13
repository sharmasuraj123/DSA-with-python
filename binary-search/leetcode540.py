nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
left = 0
right = len(nums)-1
unique = -1
if len(nums)==1:print(nums[0])
while left <= right:
    mid = (left+right)//2
    if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
        print(nums[mid])
        break
    elif nums[mid]==nums[mid-1]:
        if (mid-left-1)%2==0:
            left = mid+1
        else:
            right = mid-2
    else:
        if (right-mid-1)%2==0:
            right = mid-1
        else:
            left = mid+2     
