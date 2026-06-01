# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val: int):
        def BST(root, v):
            if root is None:
                return None
            if root.val == val:
                return root
            elif root.val > val:
                node = BST(root.left, val)
            else:
                node = BST(root.right, val)
            return node

        n = BST(root, val)
        return n
