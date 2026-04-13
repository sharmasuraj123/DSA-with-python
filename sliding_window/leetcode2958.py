# class Solution:
#     def maxSubarrayLength(self, nums: List[int], k: int) -> int:
#         hashMap = {}
#         l, r, max_size = 0, 0, 0
#         n = len(nums)
#         while r < n:
#             hashMap[nums[r]] = 1 + hashMap.get(nums[r], 0)
#             if hashMap[nums[r]] > k:
#                 max_size = max(max_size, r - l)
#                 while hashMap[nums[r]] > k:
#                     hashMap[nums[l]] = hashMap[nums[l]] - 1
#                     l += 1
#             r += 1
#         max_size = max(max_size, r - l)
#         return max_size
