# def longestSubarray(self, arr, k):
#     n = len(arr)
#     map = {}  # {prefix_sum:index}
#     map[0] = -1
#     max_size = 0
#     prefix_sum = 0
#     size = 0
#     for i in range(n):
#         prefix_sum += arr[i]
#         if prefix_sum - k in map:
#             size = i - map[prefix_sum - k]
#             max_size = max(max_size, size)
#         if prefix_sum not in map:
#             map[prefix_sum] = i
#     return max_size
  