matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
rows = len(matrix)
column = len(matrix[0])
element = -1
for r in range(rows):
    for c in range(column):
        if matrix[r][c] == 0:
            if r == 0:
                element = 0
                matrix[0][c] = 0
            else:
                matrix[r][0] = 0
                matrix[0][c] = 0

for r in range(1,rows):
    for c in range(1,column):
        if matrix[0][c] == 0 or matrix[r][0]==0:
            matrix[r][c] = 0

if matrix[0][0] == 0:
    for r in range(rows):
        matrix[r][0] = 0 

if element == 0:
    for c in range(column):
        matrix[0][c] = 0

print(matrix)                           
            
                        
                    
            
        