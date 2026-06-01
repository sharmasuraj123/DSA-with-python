class Solution:
    def Paths(self, root):
        temp, res = [], []

        def dfs(r):
            if r is None:
                return
            temp.append(r.data)
            if r.left is None and r.right is None:
                res.append(list(temp))
            else:

                dfs(r.left)
                dfs(r.right)
            temp.pop()

        dfs(root)
        return res
