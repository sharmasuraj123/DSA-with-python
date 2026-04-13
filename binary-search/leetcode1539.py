# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         count = 0
#         counting = 0
#         i = 0
#         while i < len(arr):
#             counting += 1
#             print("counting:", counting)
#             if arr[i] != counting:
#                 count += 1
#                 if count == k:
#                     return counting
#             else:
#                 i += 1
#         counting = arr[len(arr) - 1] + (k - count)
#         return counting


# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         left = 0
#         right = len(arr) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             missing_numbers = arr[mid] - mid - 1
#             if missing_numbers < k:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         missing_number = right + k + 1
#         return missing_number
