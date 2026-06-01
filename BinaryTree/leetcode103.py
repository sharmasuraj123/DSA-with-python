# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if root is None:
#             return []
#         arr, level_no = [root], 0
#         zigzag_arr = [[root.val]]
#         while arr:
#             level, i, n = [], 0, len(arr)
#             while i < n:
#                 if arr[0].left != None:
#                     arr.append(arr[0].left)
#                     level.append(arr[0].left.val)
#                 if arr[0].right != None:
#                     arr.append(arr[0].right)
#                     level.append(arr[0].right.val)
#                 arr.pop(0)
#                 i += 1
#             if level:
#                 if level_no % 2 == 0:
#                     level.reverse()
#                     zigzag_arr.append(level.copy())
#                 else:
#                     zigzag_arr.append(level.copy())
#                 level_no += 1
#         return zigzag_arr




# " THIS IS IN  O(n). "

# from collections import deque


# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if root is None:
#             return []
#         d, level_no = deque([root]), 0
#         zigzag_arr = [[root.val]]
#         while d:
#             level = []
#             l = len(d)
#             if level_no % 2 == 0:
#                 for i in range(l):
#                     node = d.popleft()
#                     if node.right:
#                         level.append(node.right.val)
#                         d.append(node.right)
#                     if node.left:
#                         level.append(node.left.val)
#                         d.append(node.left)
#             else:
#                 for i in range(l):
#                     node = d.pop()
#                     if node.left:
#                         level.append(node.left.val)
#                         d.appendleft(node.left)
#                     if node.right:
#                         level.append(node.right.val)
#                         d.appendleft(node.right)
#             if level:
#                 zigzag_arr.append(level.copy())
#             level_no += 1
#         return zigzag_arr
