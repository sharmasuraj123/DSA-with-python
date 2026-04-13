from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]
res = defaultdict(list)
# res["5"].append("suraj")
# res["5"].append("sharma")
for str in strs:
    count = [0]*26
    for i in str:
        count[ord(i)-ord("a")] += 1
    res[tuple(count)].append(str)
print(list(res.values()))

