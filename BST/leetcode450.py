# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key: int):

        def Dfs(r, key):
            if r is None:
                return None
            if r.val == key:
                if r.right != None:
                    x = r.right
                    while x.left is not None:
                        x = x.left
                    x.left = r.left
                    return r.right
                else:
                    return r.left

            if key > r.val:
                r.right = Dfs(r.right, key)
            else:
                r.left = Dfs(r.left, key)
            return r

        RootNode = Dfs(root, key)
        return RootNode
