# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):

        def valid(node, leftBoundary, rightBoundary):
            if not node:
                return True
            if not (node.val < rightBoundary and node.val > leftBoundary):
                return False

            left = valid(node.left, leftBoundary, node.val)
            right = valid(node.right, node.val, rightBoundary)

            return left and right

        return valid(root, float("-inf"), float("inf"))

        # def Inorder(r):
        #     if r is None:return
        #     Inorder(r.left)
        #     arr.append(r.val)
        #     Inorder(r.right)
        # arr = []
        # Inorder(root)

        # for i in range(len(arr)-1):
        #     if arr[i]>=arr[i+1]:return False
        # return True
