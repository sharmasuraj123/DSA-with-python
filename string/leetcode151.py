s = "  the   sky is blue   "
# s2 = s.strip()
# new_s = ""
# idx1 = 0
# idx2 = 0
# temp = ""
# space_count = 0
# for i in range(len(s2)):
#     if s2[i]!=' ':
#         temp+=s2[i]
#         space_count = 0
#     else:
#         space_count +=1
#         if space_count<2:
#             new_s = temp+" "+new_s
#             temp = ""
# new_s = temp + " " + new_s
# print(new_s)        


new_s = ""
i = len(s)-1

while i>=0:
    while i>=0 and s[i]==' ':
        i-=1    
    if i<0:
        break    
    strigEnd = i
    while i>=0 and s[i]!=' ':
        i-=1
    stringStart = i+1
    part = s[stringStart:strigEnd+1]
    if new_s=="":
        new_s+=part
    else:
        new_s= new_s+" "+part    
print(new_s)        
        
            