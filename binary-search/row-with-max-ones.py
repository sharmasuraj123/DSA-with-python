arr = [
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
]
row = len(arr)
column = len(arr[0])
max_sum = 0
ans_row = -1
for i in range(row):
    sum = 0
    for j in range(column):
        sum+=arr[i][j]
    if sum>max_sum:
        ans_row = i
        max_sum = sum
print(ans_row)        
