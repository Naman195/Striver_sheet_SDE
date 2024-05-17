def generateRow(row):
    ans = 1
    rowList = []
    rowList.append(1)
    for i in range(1, row):
        ans = ans * (row-i)
        ans = ans // i
        rowList.append(ans)
    return rowList

def printtriangle(n):
    ans = []
    for row in range(1, n+1):
        ans.append(generateRow(row))
    return ans
    
    
print(printtriangle(6))