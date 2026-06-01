# lass Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         idx = len(inorder)-1

#         def Tree(inorder,postorder):
#             nonlocal idx
#             if idx<0 or len(inorder)==0:return None
#             root = TreeNode(postorder[idx])
#             idx-=1
#             root_node = inorder.index(root.val)
#             root.right = Tree(inorder[root_node+1:],postorder)
#             root.left = Tree(inorder[:root_node],postorder)
#             return root
#         r = Tree(inorder,postorder) 
#         return r   

        