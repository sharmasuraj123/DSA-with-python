# Must need extra memory

nums = [3, 1, -2, -5, 2, -4]
List = [0]*len(nums)
positive = 0
negative = 1
for i in nums:
    if i>0:
        List[positive] = i
        positive+=2
    else:
        List[negative] = i  
        negative+=2
print(List)          

