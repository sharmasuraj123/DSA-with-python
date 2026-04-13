# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         min_length = len(strs[0])
#         for x in strs:
#             if len(x) < min_length:
#                 min_length = len(x)

#         str = ""
#         for i in range(min_length):
#             j = 0
#             while j < len(strs) - 1:
#                 if strs[j][i] != strs[j + 1][i]:
#                     return str
#                 j += 1
#             str = str + strs[j][i]
#         return str
