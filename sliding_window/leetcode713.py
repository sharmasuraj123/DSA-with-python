nums = [10, 5, 2, 6]
k = 100
l,r,count,n = 0,0,0,len(nums)
product = 1
while r<n:
    product*=nums[r]
    while product>=k and l<=r:
        product/=nums[l]
        l += 1
        if product<k:
            break
    count+=r-l+1
    r+=1
print(count)            
