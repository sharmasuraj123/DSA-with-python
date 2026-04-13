from collections import defaultdict
s = "f11"
t = "b23"
Hashmap = defaultdict()
for i in range(len(s)):
    if s[i] == t[i]:
        Hashmap[s[i]] = t[i]
    if Hashmap.get(s[i],0)==0 and   
    elif Hashmap.get(s[i],0)!=t[i] and Hashmap.get(t[i],0)==0:
        Hashmap[s[i]] = t[i]
        Hashmap[t[i]] = s[i]

print(True)        
