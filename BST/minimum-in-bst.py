"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""


class Solution:
    def minValue(self, root):
        if root is None:
            return -1

        def BST(root, mini):
            if root is None:
                return mini
            mini = min(mini, BST(root.left, root.data))
            return mini

        minimum_val = BST(root, root.data)
        return minimum_val
