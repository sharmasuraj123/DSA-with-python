# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count = 0
#         Map = {}
#         Map[0] = 1
#         sum = 0
#         for i in nums:
#             sum += i
#             if sum - k in Map:
#                 count += Map[sum - k]
#             Map[sum] = 1 + Map.get(sum, 0)
#         return count
