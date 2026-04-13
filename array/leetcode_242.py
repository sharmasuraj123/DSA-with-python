# s = "anagram"
# t = "nagaram"
# s_sorted = "".join(sorted(s))
# t_sorted = "".join(sorted(t))

# print(s_sorted==t_sorted)
# print(sorted(s)==sorted(t))
# print((sorted(s)))


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # s_sorted = "".join(sorted(s))
#         # t_sorted = "".join(sorted(t))
#         # return s_sorted==t_sorted                     # THIS IS O(NLOGN) AND O(N)
#         return sorted(s) == sorted(t)


# class Solution:                                          # THIS IS O(N) AND O(N)
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         counterS, counterT = {}, {}
#         for x in range(len(s)):
#             counterS[s[x]] = 1 + counterS.get(s[x], 0)
#             counterT[t[x]] = 1 + counterT.get(t[x], 0)
#         for x in counterS:
#             if counterS[x] != counterT.get(x, 0):
#                 return False
#         return True

# s = {7:0}
# if s.get(7):
#     print("hello") 