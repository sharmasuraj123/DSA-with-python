from collections import defaultdict
s = "Abab"
hash = defaultdict(int)
for i in s:
    hash[i]+=1
sorted_hash = dict(sorted(hash.items(),key=lambda x:x[1],reverse=True))
arr = ""
for x,y in sorted_hash.items():
    arr+=x*y
print(arr)
      

