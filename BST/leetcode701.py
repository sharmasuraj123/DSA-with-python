# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root, val: int):
        if not root:
            return TreeNode(val)

        def dfs(r, val):
            if r is None:
                return None
            if r.val > val:
                left = dfs(r.left, val)
                if left is None:
                    x = TreeNode(val)
                    r.left = x
            else:
                right = dfs(r.right, val)
                if right is None:
                    x = TreeNode(val)
                    r.right = x
            return r

        r = dfs(root, val)
        return r
