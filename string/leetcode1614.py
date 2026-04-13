s = "()(())((()()))"
max_count = 0
count = 0
for i in s:
    if i=='(':
        count+=1
    elif i==')':
        max_count = max(max_count,count)
        count-=1
print(max_count)             
