class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        hashMap = dict()

        def dfs(r, h):
            nonlocal hashMap
            if r is None:
                return
            if h not in hashMap:
                hashMap[h] = r.val
            dfs(r.right, h + 1)
            dfs(r.left, h + 1)

        dfs(root, 0)
        x = [val for idx, val in hashMap.items()]
        return x
