# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         maxi = float("-inf")

#         def dfs(r):
#             nonlocal maxi
#             if not r:
#                 return 0
#             left = max(0, dfs(r.left))
#             right = max(0, dfs(r.right))
#             maxi = max(maxi, left + right + r.val)
#             return max(left, right) + r.val

#         ans = dfs(root)
#         return ans
