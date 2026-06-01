"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""


class Solution:
    def findMaxFork(self, root, k):
        # code here

        def DFS(r, k, floor):
            if r is None:
                return -1
            if r.data == k:
                return k
            if r.data < k:
                floor = max(floor, r.data, DFS(r.right, k, floor))
            else:
                floor = DFS(r.left, k, floor)
            return floor

        floor = -1
        f = DFS(root, k, floor)
        return f
