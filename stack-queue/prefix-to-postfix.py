# class Solution:
#     def preToPost(self, pre_exp):
#         s = "".join(reversed(pre_exp))
#         st = []
#         for i in s:
#             if "a" <= i <= "z" or "0" <= i <= "9" or "A" <= i <= "Z":
#                 st.append(i)
#             else:
#                 a = st.pop()
#                 b = st.pop()
#                 val = a + b + i
#                 st.append(val)
#         return st.pop()
       
