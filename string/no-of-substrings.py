s = "abcccba"
last = [-1]*3
count = 0
for i in range(len(s)):
    last[ord(s[i])-ord("a")] = i
    if last[0]!=-1 and last[1]!=-1 and last[2]!=-1:
        count+=(1+min(last[0],last[1],last[2]))
print(count)
