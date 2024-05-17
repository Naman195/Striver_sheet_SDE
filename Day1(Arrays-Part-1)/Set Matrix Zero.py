matrix=[[1,1,1],
        [1,0,1],
        [1,1,1]]

# Output:
#  [[1,0,1]
# ,[0,0,0],
# [1,0,1]]


def setZero(matrix):
    n = len(matrix)
    m = len(matrix[0])
    row = []
    col = []
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)
    
    for i in range(n):
        for j in range(m):
            if i in row or j in col:
                matrix[i][j] = 0
setZero(matrix)
print(matrix)    
                
                