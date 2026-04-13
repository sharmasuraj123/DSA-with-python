# from queue import LifoQueue


# class Solution:
#     def isValid(self, s: str) -> bool:
#         self.st = LifoQueue()
#         for i in s:
#             if i == ")":
#                 if self.st.empty():
#                     return False
#                 else:
#                     a = self.st.get()
#                     if a != "(":
#                         return False
#             elif i == "]":
#                 if self.st.empty():
#                     return False
#                 else:
#                     a = self.st.get()
#                     if a != "[":
#                         return False
#             elif i == "}":
#                 if self.st.empty():
#                     return False
#                 else:
#                     a = self.st.get()
#                     if a != "{":
#                         return False
#             else:
#                 self.st.put(i)
#         return self.st.empty()
