# class Solution:
#     def postToPre(self, post_exp):
#         st = []
#         for i in post_exp:
#             if "a" <= i <= "z" or "A" <= i <= "Z" or "0" <= i <= "9":
#                 st.append(i)
#             else:
#                 a = st.pop()
#                 b = st.pop()
#                 val = i + b + a
#                 st.append(val)
#         return st.pop()
