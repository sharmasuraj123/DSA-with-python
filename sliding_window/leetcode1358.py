s = "abcabc"
count, l, r, n, hashMap = 0, 0, 0, len(s), {}
while r < n:
    hashMap[s[r]] = hashMap.get(s[r],0)+1
    while len(hashMap) >= 3 and l <= r:
        count += (n - r)
        hashMap[s[l]] = hashMap.get(s[l],0)-1
        if hashMap[s[l]]==0:
            hashMap.pop(s[l])
        l += 1
        print(n - r)
    r += 1
print(count)
