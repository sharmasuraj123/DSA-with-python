# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        invalid = False

        def backtrack(r):
            nonlocal invalid
            if r is None:
                return 0
            left_count = backtrack(r.left)
            right_count = backtrack(r.right)
            v = abs(left_count - right_count)
            if v >= 2:
                invalid = True
            return 1 + max(left_count, right_count)

        V = backtrack(root)
        if invalid:
            return False
        else:
            return True
