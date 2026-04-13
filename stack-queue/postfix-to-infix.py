# class Solution:
#     def postToInfix(self, postfix):
#         st = []
#         for i in postfix:
#             if "a" <= i <= "z" or "A" <= i <= "Z" or "0" <= i <= "9":
#                 st.append(i)
#             else:
#                 a = st.pop()
#                 b = st.pop()
#                 val = "(" + b + i + a + ")"
#                 st.append(val)
#         return st.pop()
