"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

from collections import deque
class Solution:
    def topView(self, root):
        hashMap = {}
        d = deque([(root, 0)])
        min_col, max_col = 0, 0

        while d:
            node, col = d.popleft()
            min_col, max_col = min(min_col, col), max(max_col, col)
            if col not in hashMap:
                hashMap[col] = node.data
            if node.left:
                d.append((node.left, col - 1))

            if node.right:
                d.append((node.right, col + 1))
        res = [hashMap[i] for i in range(min_col, max_col + 1)]
        return res
