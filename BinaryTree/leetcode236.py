# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        def dfs(r, p, q):
            if r is None:
                return None
            if r.val == p or r.val == q:
                return r

            leftLca = dfs(r.left, p, q)
            rightLca = dfs(r.right, p, q)

            if leftLca and rightLca:
                return r
            elif leftLca:
                return leftLca
            else:
                return rightLca

        lca = dfs(root, p.val, q.val)
        return lca
