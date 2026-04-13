s = "aabcb"
total = 0
for i in range(len(s)):
    hash = {}
    for j in range(i, len(s)):
        hash[s[j]] = 1 + hash.get(s[j], 0)
        values = hash.values()
        maxi = max(values)
        mini = min(values)
        total += maxi - mini
print(total)        
