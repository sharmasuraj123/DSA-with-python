import math
nums = [44, 22, 33, 11, 1]
threshold = 5
min_divisor = max(nums)
left  = 1
right = max(nums)
while left<=right:
    mid = (left+right)//2
    sum = 0
    for i in nums:
        sum += math.ceil(i/mid)
    if sum<=threshold:
        min_divisor = min(min_divisor,mid)
        right = mid-1
    else:left = mid+1
print(min_divisor)              
