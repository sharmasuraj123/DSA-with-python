arr = [3, 1, 2,4]
ans = 0
subarr = []
for i in range(len(arr)):
    for j in range(i,len(arr)):
        x = arr[i:j+1]
        subarr.append(x.copy())
total_sum = 0        
for i in subarr:
    print(min(i))
    total_sum+=min(i)
    print(total_sum)           
total_sum = total_sum%(10**9+7)        
print(ans)