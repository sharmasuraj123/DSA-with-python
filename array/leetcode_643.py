nums = [0,1,1,3,3]
k = 4
sum = 0
avg = -1000000000000000
count = 0
ind = 0

for i in nums:
    sum += i
    if(count<k):
        count+=1
    elif(count==k): # count = 4
        avg = max(avg,sum/k)
        sum-=nums[ind]
        ind+=1

print(avg)        
