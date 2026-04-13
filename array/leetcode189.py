# nums = [-1, -100, 3, 99]
# doubles = nums*2
# size = len(nums)
# k = 2
# i = size-k
# j = i+size
# nums[0:size] = doubles[i:j]
# print(nums)

nums = [-1, -100, 3, 99]
k = 2
nums.reverse()
nums[0:k] = reversed(nums[0:k])
nums[k : len(nums)] = reversed(nums[k : len(nums)])

print(nums)