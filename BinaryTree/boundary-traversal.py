"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
"""


class Solution:
    def findleft_nd(self, r, result):
        if (not r) or (r.left == None and r.right == None):
            return
        result.append(r.data)
        if not r.left:
            self.findleft_nd(r.right, result)

        else:
            self.findleft_nd(r.left, result)

    def findright_nd(self, r, result):
        if (not r) or (r.left == None and r.right == None):
            return
        if not r.right:
            self.findright_nd(r.left, result)
        else:
            self.findright_nd(r.right, result)
        result.append(r.data)

    def findleaf_nd(self, r, result):
        if not r:
            return
        self.findleaf_nd(r.left, result)
        self.findleaf_nd(r.right, result)
        if r.left == None and r.right == None:
            result.append(r.data)

    def boundaryTraversal(self, root):
        if not root:
            return []
        result = [root.data]
        self.findleft_nd(root.left, result)
        if root.left or root.right:
            self.findleaf_nd(root, result)
        self.findright_nd(root.right, result)
        return result
