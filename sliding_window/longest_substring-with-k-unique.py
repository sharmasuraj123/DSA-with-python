# class Solution:
#     def longestKSubstr(self, s, k):
#         hashMap = {}
#         l, r, count, n, max_len = 0, 0, 0, len(s), -1
#         togal = False
#         while r < n:
#             hashMap[s[r]] = hashMap.get(s[r], 0) + 1
#             while len(hashMap) > k:
#                 togal = True
#                 max_len = max(max_len, r - l)
#                 hashMap[s[l]] = hashMap.get(s[l], 0) - 1
#                 if hashMap[s[l]] == 0:
#                     hashMap.pop(s[l])
#                 l += 1
#             r += 1
#         if togal or len(hashMap) >= k:
#             max_len = max(max_len, r - l)
#             return max_len
#         return -1
