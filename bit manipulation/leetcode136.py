nums = [2,2,1]
answer = nums[0]
for i in range(1,len(nums)):
    answer^=nums[i]
print(answer) 