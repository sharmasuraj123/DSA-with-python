# class Solution:
#     def findSubset(self, candidates, idx, res, temp, target):
#         if idx == len(candidates):
#             if target == 0:
#                 res.append(temp.copy())
#             return
#         if candidates[idx] <= target:
#             temp.append(candidates[idx])
#             self.findSubset(candidates, idx, res, temp, target - candidates[idx])
#             temp.pop()
#         self.findSubset(candidates, idx + 1, res, temp, target)

#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         temp = []
#         self.findSubset(candidates, 0, res, temp, target)
#         return res
