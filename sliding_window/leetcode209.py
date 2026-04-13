# min_length,l,r,n,sum = len(nums)+1,0,0,len(nums),0
# while r<n:
#     sum+=nums[r]
#     while sum>=target and l<=r:
#         min_length = min(min_length,r-l+1)
#         sum-=nums[l]
#         l+=1
#     r+=1
# if min_length>n:return 0        
# return min_length