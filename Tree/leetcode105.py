# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         idx = 0

#         def Tree(inorder, preorder):
#             nonlocal idx
#             if idx >= len(preorder) or len(inorder) == 0:
#                 return None
#             root = TreeNode(preorder[idx])
#             rootIdx = inorder.index(root.val)
#             idx += 1
#             root.left = Tree(inorder[:rootIdx], preorder)
#             root.right = Tree(inorder[rootIdx + 1 :], preorder)
#             return root

#         r = Tree(inorder, preorder)
#         return r
