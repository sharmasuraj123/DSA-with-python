arr = [1, 2, 3, 5]
arr_sum = 0
for i in arr:
    arr_sum+=i

size = len(arr)+1
total_sum = (size*(size+1))//2
print(total_sum-arr_sum)