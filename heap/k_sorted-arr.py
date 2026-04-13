arr = [13, 8, 10, 7, 15, 14, 12]
k = 1
hashMap = {}
for i in range(len(arr)):
    hashMap[arr[i]] = i
arr.sort()
for i in range(len(arr)):
    if abs(hashMap[arr[i]]-i)>k:
        print("No")
        break

print("Yes")    
