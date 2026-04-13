arr = [-838 ,- 329]
if len(arr)==1:
    if arr[0]<0:print(-1)
    else:print(arr)

sum = 0
max_sum = -10000000
length = 0
max_length = 0
i,j,idx1,idx2 = 0,0,0,0
for k in range(len(arr)):
    if arr[k]>=0:
        sum+=arr[k]
        length+=1
        j = k
        if sum>max_sum:
            idx1 = i
            idx2 = j
            max_sum = sum
            max_length = length
        elif sum == max_sum and length > max_length:
            idx1 = i
            idx2 = j
            max_length = length
    else:
        sum = 0
        length = 0
        i = k + 1
        j = k + 1
if max_sum < 0:
    print(-1)
else:print(arr[idx1:idx2+1])     
