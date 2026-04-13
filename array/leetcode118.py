numRow = 6
if numRow==1:print([[1]])
elif numRow == 2:print([[1],[1,1]])
else:
    matrix = [[1],[1,1]]
    for r in range(2,numRow+1):
        arr = []
        arr.append(1)
        for c in range(1,r):
            sum = matrix[r-1][c-1] + matrix[r-1][c]
            arr.append(sum)
        arr.append(1) 
        matrix.append(arr) 
    print(matrix)          
