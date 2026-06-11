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

        def Dfs(node, p, q):
            if node.val > p.val and node.val > q.val:
                return Dfs(node.left, p, q)
            if node.val < p.val and node.val < q.val:
                return Dfs(node.right, p, q)
            if node.val == p.val:
                return p
            if node.val == q.val:
                return q
            return node

        return Dfs(root, p, q)
