# class Solution:
#     def preToInfix(self, pre_exp):
#         s = "".join(reversed(pre_exp))
#         st = []
#         for i in s:
#             if "a" <= i <= "z" or "A" <= i <= "Z" or "0" <= i <= "9":
#                 st.append(i)
#             else:
#                 a = st.pop()
#                 b = st.pop()
#                 value = "(" + a + i + b + ")"
#                 st.append(value)
#         return st.pop()
