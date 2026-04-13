nums = [1, 1, 0, 1, 1, 1]
count = 0
consecutive = 0

for i in nums:
    if i!=1:
        consecutive = max(consecutive,count)
        count = 0
    else:
        count+=1
consecutive = max(consecutive,count)        
           
        