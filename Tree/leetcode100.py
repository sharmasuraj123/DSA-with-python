# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if q is None and p is None:
#             return True
#         check = False

#         def dfs(root1, root2):
#             nonlocal check
#             if root1 == None and root2 == None:
#                 return
#             if (root1 == None and root2 != None) or (root1 != None and root2 == None):
#                 check = True
#                 return
#             if root1.val == root2.val:
#                 dfs(root1.left, root2.left)
#                 dfs(root1.right, root2.right)
#             else:
#                 check = True
#                 return

#         dfs(p, q)
#         return not check
