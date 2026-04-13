from collections import defaultdict

nums = [3,4,4,3,2,1,4,2,2,2,4]
majority = len(nums)/3
hashMap = defaultdict(int)

for i in nums:
    hashMap[i] = 1 + hashMap.get(i,0)
newarr = [i for i in hashMap if hashMap[i] > majority]
