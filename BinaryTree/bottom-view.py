"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
"""
from collections import deque

class Solution:
    def bottomView(self, root):
        if not root:
            return []
        hashMap = {}
        d = deque([(root, 0)])
        max_col, min_col = 0, 0
        while d:
            node, col = d.popleft()
            min_col, max_col = min(min_col, col), max(max_col, col)
            hashMap[col] = node.data
            if node.left:
                d.append((node.left, col - 1))
            if node.right:
                d.append((node.right, col + 1))
        res = []
        for i in range(min_col, max_col + 1):
            res.append(hashMap[i])
        return res
