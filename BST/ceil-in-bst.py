"""
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""


class Solution:
    def findCeil(self, root, x):

        def DFS(r, x, ceil):
            if r is None:
                return 10**5
            if r.data == x:
                return x
            if r.data > x:
                ceil = min(ceil, r.data, DFS(r.left, x, ceil))
            else:
                ceil = DFS(r.right, x, ceil)
            return ceil

        ceil = 10**5
        c = DFS(root, x, ceil)
        return -1 if c == 10**5 else c
