# nums = [2, 1, 3, 4]
# pivot = 0
# for i in range(len(nums)-1):
#     if nums[i]>nums[i+1]:
#         pivot = i+1
# if pivot ==0:print(True)
# nums[0:pivot] = reversed(nums[0:pivot])
# nums[pivot:len(nums)] = reversed(nums[pivot:len(nums)])
# nums.reverse()
# for i in range(len(nums)-1):
#     if nums[i]>nums[i+1]:print(False)
# print(True)



# neetcode 
# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         count = 1
#         size = len(nums)
#         if size == 1:
#             return True
#         for i in range(1, size * 2):
#             if count == size:
#                 return True
#             if nums[(i - 1) % size] <= nums[i % size]:
#                 count += 1
#             else:
#                 count = 1
#         return False
