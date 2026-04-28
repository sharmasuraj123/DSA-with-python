class Solution:
    def checkSubsequenceSum(self, N, arr, K):

        def backtracking(arr, idx, target):

            if target == 0:
                return True
            if target < 0:
                return False

            if idx == len(arr):
                return target == 0
            r1 = backtracking(arr, idx + 1, target - arr[idx])
            r2 = backtracking(arr, idx + 1, target)
            return r1 or r2

        result = backtracking(arr, 0, K)
        return "Yes" if result else "No"
