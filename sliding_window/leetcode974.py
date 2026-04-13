nums = [4, 5, 0, -2, -3, 1]
k = 5

for i in range(1,len(nums)):
    nums[i] += nums[i-1]
for i in range(len(nums)):
    nums[i]%=k
hashMap,count = {},0
for i in range(len(nums)):
    if nums[i]==0:count+=1
    if nums[i] in hashMap:
        count += hashMap[nums[i]]
    hashMap[nums[i]] = hashMap.get(nums[i],0)+1
print(count)    
        
