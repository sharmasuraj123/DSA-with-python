# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

#         if not root:
#             return []
#         q = deque([(root, 0, 0)])
#         min_col, max_col = 0, 0
#         cols = defaultdict(list)

#         while q:
#             node, row, col = q.popleft()
#             min_col, max_col = min(min_col, col), max(max_col, col)
#             cols[col].append((row, node.val))

#             if node.left:
#                 q.append((node.left, row + 1, col - 1))
#             if node.right:
#                 q.append((node.right, row + 1, col + 1))

#         res = []
#         for i in range(min_col, max_col + 1):
#             cols[i].sort()
#             x = [val[1] for val in cols[i]]
#             res.append(x)
#         return res

#         # if not root:return []
#         # q = deque([(root,0,0)])  # (root,col)
#         # min_col,max_col = 0,0
#         # cols = defaultdict(list) # cols index -> list of values.

#         # while q:
#         #     node,row,col = q.popleft()
#         #     min_col,max_col = min(min_col,col),max(max_col,col)
#         #     cols[col].append((row,node.val))

#         #     if node.left:
#         #         q.append((node.left,row+1,col-1))
#         #     if node.right:
#         #         q.append((node.right,row+1,col+1))

#         # result = []
#         # for i in range(min_col,max_col+1):
#         #     cols[i].sort()
#         #     x = [val[1] for val in cols[i]]
#         #     result.append(x)
#         # return result
