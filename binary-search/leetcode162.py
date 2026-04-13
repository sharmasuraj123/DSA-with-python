nums = [1, 2, 3, 1]
if len(nums)==1:
    print(0)
if nums[0]>nums[1]:
    print(0) 
if nums[len(nums)-1]>nums[len(nums)-2]:
    print(len(nums)-1)
left = 0
right = len(nums)-1
while left<=right:
    mid = (left+right)//2
    if nums[mid-1]<nums[mid]>nums[mid+1]:
        print(mid)
        break
    elif nums[mid]>nums[mid-1]:
        left = mid+1
    else:
        right = mid-1    
                   