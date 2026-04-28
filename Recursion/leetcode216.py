class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def Backtrack(idx, k, n, res, curr):
            if len(curr) == k:
                if n == 0:
                    res.append(curr.copy())
                return
            if n <= 0:
                return
            prev = -1
            for i in range(idx, 10):
                if i == prev:
                    continue
                curr.append(i)
                Backtrack(i + 1, k, n - i, res, curr)
                curr.pop()
                prev = i

        Backtrack(1, k, n, res, [])
        return res
