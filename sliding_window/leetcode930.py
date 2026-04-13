# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         # atleast goal
#         count1, l, r, n, sum = 0, 0, 0, len(nums), 0
#         while r < n:
#             sum += nums[r]
#             while sum >= goal and l <= r:
#                 count1 += n - r
#                 sum -= nums[l]
#                 l += 1
#             r += 1

#         # atleast goal+1
#         count2, l, r, sum = 0, 0, 0, 0
#         while r < n:
#             sum += nums[r]
#             while sum >= (goal + 1) and l <= r:
#                 count2 += n - r
#                 sum -= nums[l]
#                 l += 1
#             r += 1
#         return count1 - count2
