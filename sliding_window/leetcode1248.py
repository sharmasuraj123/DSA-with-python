# class Solution:
#     def numberOfSubarrays(self, nums: List[int], k: int) -> int:
#         # atleast k odd
#         count1, l, r, n, odds = 0, 0, 0, len(nums), 0
#         while r < n:
#             if nums[r] % 2 != 0:
#                 odds += 1
#             while odds >= k and l <= r:
#                 count1 += n - r
#                 if nums[l] % 2 != 0:
#                     odds -= 1
#                 l += 1
#             r += 1

#         # atleast k+1 odd
#         count2, l, r, odds = 0, 0, 0, 0
#         while r < n:
#             if nums[r] % 2 != 0:
#                 odds += 1
#             while odds >= (k + 1) and l <= r:
#                 count2 += n - r
#                 if nums[l] % 2 != 0:
#                     odds -= 1
#                 l += 1
#             r += 1
#         return count1 - count2
