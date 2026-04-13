nums = [1,2,1,2,3]
total1,l,r,n = 0,0,0,len(nums)
hashMap = {}
# atleast k element
while r<n:
    hashMap[nums[r]] = hashMap.get(nums[r],0)+1
    while len(hashMap)>=k:
        total1+=n-r
        hashMap[nums[l]] = hashMap.get(nums[l],0)-1
        if hashMap[nums[l]]==0:
            hashMap.pop(nums[l])
        l+=1
    r+=1
# atleast k+1 
hashMap.clear()   
total2,l,r = 0,0,0
while r<n:
    hashMap[nums[r]] = hashMap.get(nums[r],0)+1
    while len(hashMap)>=k+1:
        total2+=n-r
        hashMap[nums[l]] = hashMap.get(nums[l],0)-1
        if hashMap[nums[l]]==0:
            hashMap.pop(nums[l])
        l+=1
    r+=1
print(total1-total2)    
