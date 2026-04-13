# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         count = 0
#         for i in nums:
#             if i!=val:
#                 count+=1

#         i,j = len(nums)-1,0
#         while j<i:
#             if nums[j]!=val:
#                 j+=1
#             elif nums[i]==val:
#                 i-=1
#             else:
#                 nums[i],nums[j] = nums[j],nums[i]
#                 i-=1
#                 j+=1
#         return count        



'''
neetcode appproch
'''

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         k = 0
#         for i in range(len(nums)):
#             if nums[i]!=val:
#                 nums[k] = nums[i]
#                 k+=1
#         return k 