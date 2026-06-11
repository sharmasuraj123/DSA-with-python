"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


class Solution:
    def findPreSuc(self, root, key):
        pre, post = None, None

        def dfs(r, key):
            nonlocal pre, post
            if r is None:
                return
            if r.data < key:
                pre = r
                return dfs(r.right, key)
            if r.data > key:
                post = r
                return dfs(r.left, key)

            if r.data == key:
                dfs(r.left, key)
                dfs(r.right, key)
                return

        dfs(root, key)
        return [pre, post]
