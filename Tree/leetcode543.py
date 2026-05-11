# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0

#         def count_level(root):
#             if root == None:
#                 return 0
#             count, arr = 0, [root]
#             while arr:
#                 count += 1
#                 n, i = len(arr), 0
#                 while i < n:
#                     if arr[0].left != None:
#                         arr.append(arr[0].left)
#                     if arr[0].right != None:
#                         arr.append(arr[0].right)
#                     i += 1
#                     arr.pop(0)
#             return count

#         maxi, length = 0, 0

#         def dfs(root):
#             nonlocal maxi
#             if root is None:
#                 return

#             dfs(root.left)
#             dfs(root.right)
#             maxi = max(maxi, count_level(root.left) + count_level(root.right))

#         dfs(root)
#         return maxi
