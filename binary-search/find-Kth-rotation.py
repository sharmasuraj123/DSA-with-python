arr = [5, 0, 2, 3, 4]
minimum = 10**7+1
left = 0
right = len(arr)-1
idx = 0
minimum1 = 10**7 + 1
while left <= right:
    mid = (left+right)//2
    minimum = min(minimum,arr[mid])
    if minimum !=minimum1:
        idx = mid
        minimum1 = minimum
    if arr[mid]>=arr[left]:
        minimum = min(minimum, arr[left])
        if minimum !=minimum1:
            idx = mid
            minimum1 = minimum
        left = mid+1
    else:
        right = mid-1
print(idx)        
