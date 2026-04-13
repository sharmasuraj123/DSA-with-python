# max_size,l,r = 0,0,0
#         charSet = set()
#         while r<len(s):
#             while s[r] in charSet:
#                 max_size = max(max_size,r-l)
#                 charSet.remove(s[l])
#                 l+=1
#             else:charSet.add(s[r])
#             r+=1
#         max_size = max(max_size,r-l)
#         return max_size                





#         final_str_length = 0
#         for i in range(len(s)):
#             string = ""
#             size = 0
#             for j in range(i,len(s)):
#                 if s[j] not in string:
#                     string+=s[j]
#                     size+=1
#                 else: 
#                     final_str_length = max(final_str_length,size)
#                     break
#                 final_str_length = max(final_str_length,size)    
#         return final_str_length              

