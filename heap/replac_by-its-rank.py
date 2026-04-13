N = 6
arr = [20, 15, 26, 2, 98, 6]
hashMap = {}
arr2 = arr.copy()
arr.sort()

for i in range(len(arr)):
    if arr[i] not in hashMap:
        hashMap[arr[i]] = i
print(hashMap, arr, arr2)
for i in range(len(arr2)):
    arr2[i] = (hashMap[arr2[i]]+1)
print(arr2)
