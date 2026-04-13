# nums = [2,2,4,5,5]
# Dict = {}
# for  i in nums:
#     Dict[i] = 1 + Dict.get(i,0)
# for i in Dict:
#     if Dict[i]==1:
#         print(i)


# nums = [3,3,4,5,5]
# Set = set()
# sum = 0
# nums_sum = 0

# for i in nums:
#     if i not in Set:
#         sum+=i
#     Set.add(i)
#     nums_sum+=i
# print(2*sum-nums_sum)

nums = [3, 3, 4, 5, 5]

element = nums[0]
for i in range(1,len(nums)):
    element = element^nums[i]
print(element)    
