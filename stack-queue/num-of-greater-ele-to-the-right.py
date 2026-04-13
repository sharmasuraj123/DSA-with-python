arr, indices = [3, 4, 2, 7, 5, 8, 10, 6], [0, 5]
output = []
for i in indices:
    x,count = arr[i],0
    for j in range(i,len(arr)):
        if arr[j]>x:count+=1
    output.append(count)
print(output)        
