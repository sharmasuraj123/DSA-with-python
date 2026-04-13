s = "(()())(())"
if len(s)==0 or len(s)==2:print("")
count = 0
final_s = ""
for i in s:
    if i=='(':
        if count>0:
            final_s+=i
        count+=1
    elif i==')':
        count-=1
        if count>0:
            final_s+=i
print(final_s)                    
            




