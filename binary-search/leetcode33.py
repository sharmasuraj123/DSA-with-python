# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#         return -1


# Hint: Find the sorted part of the array


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left = 0
#         end = len(nums) - 1
#         right = len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[left] <= nums[mid]:
#                 if nums[left] <= target < nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             else:
#                 if nums[mid] < target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#         return -1


nums = [2, 5, 6, 0, 0, 1, 2]
target  = 6
left = 0
end = len(nums)-1
right = len(nums)-1
while left<=right:
    mid = (left+right)//2
    if nums[mid]==target:
        print(True)
        break
    elif nums[left]<=nums[mid]:
        if nums[left]<=target<nums[mid]:
            right = mid - 1
        else:
            left = mid + 1 
    else:
        if nums[mid]<target<=nums[right]:
            left = mid+1
        else:
            right = mid-1              
