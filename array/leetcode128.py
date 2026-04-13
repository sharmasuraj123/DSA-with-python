#   count = 1
#         max_count = 1
#         nums.sort(reverse=False)
#         if len(nums)==1 or len(nums)==0:return len(nums)
#         for i in range(1,len(nums)):
#             if nums[i-1]==nums[i]-1:
#                 count+=1
#             elif nums[i-1]==nums[i]:
#                 count = count    
#             else:
#                 max_count = max(max_count,count)  
#                 count = 1 
#         max_count = max(max_count,count)        
#         return max_count


#optimal 

nums = [100,4,200,1,3,1,2]
length = 0
max_length = 0
Set = set()
for i in nums:
    Set.add(i)
    
for x in Set:
    val = x - 1
    if val not in Set:
        length = 1
        k = 1
        while True:
            if x+k in Set:
                length+=1
                k+=1
            else:
                max_length = max(max_length,length)
                length = 0
                break
print(max_length)                
        
    