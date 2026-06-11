class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):

        def DFS(left, right, arr):
            if left > right:
                return None
            mid = (left + right) // 2
            x = TreeNode(arr[mid])
            x.left = DFS(left, mid - 1, arr)
            x.right = DFS(mid + 1, right, arr)
            return x

        root = DFS(0, len(nums) - 1, nums)
        return root
