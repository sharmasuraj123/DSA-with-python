matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
n = len(matrix)
for r in range(n):
    for c in range(r+1,n):
        matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

for i in range(n):
    matrix[i].reverse()
print(matrix)    