nums = [3, 2, 1]
nums.reverse()
print(nums)
# index = -1
# i = len(nums)-2
# while i>=0:
#     if nums[i]<nums[i+1]:
#         index = i
#         break
#     i-=1
# if index==-1:
#     nums.reverse()
# for i in range(len(nums)-1,index,-1):
#     if nums[i]>nums[index]:
#         nums[i],nums[index] = nums[index],nums[i]
#         break
# nums[index + 1 :] = reversed(nums[index + 1 :])
# print(nums)

# from itertools import permutations


# class Solution:
#     # Function to find the next permutation
#     def nextPermutation(self, nums):
#         # Generate all unique permutations
#         perms = sorted(set(permutations(nums)))

#         # Convert list to tuple for comparison
#         current = tuple(nums)

#         # Traverse the list
#         for i in range(len(perms)):
#             if perms[i] == current:
#                 # If last permutation, return first
#                 if i == len(perms) - 1:
#                     return list(perms[0])
#                 # Else return next
#                 return list(perms[i + 1])
