# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int): 

        def Inorder(r):
            if r is None:
                return
            Inorder(r.left)
            arr.append(r.val)
            Inorder(r.right)

        arr = []
        Inorder(root)
        for i in range(len(arr)):
            if i == k - 1:
                return arr[i]
