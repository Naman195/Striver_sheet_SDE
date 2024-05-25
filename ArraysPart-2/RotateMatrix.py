matrix = [[1,2,3],[4,5,6],[7,8,9]]

def rotate(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        for j in range(i+1, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in matrix:
        i.reverse()
    print(matrix)


rotate(matrix)