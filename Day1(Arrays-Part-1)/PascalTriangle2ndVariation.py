# row no is given and print entire nth row
def nCr(row, col):
    res = 1
    for i in range(col): # run till col = 2 times
        res = res * (row - i) # res = 1 * (7-i) i =0
        res = res // (i+1)  # res = res // (i+1) => i = 1
    return res

def printEntireRow(n):
    for c in range(1, n+1):
        print(nCr(n-1, c-1), end = " ")
    
        

print(printEntireRow(6))




# optimize
def printRow(n):
    ans = 1
    print(ans, end = " ")
    for i in range(1, n):
        ans = ans * (n-i)
        ans = ans // (i)
        print(ans, end = " ")
    # return ans

# print(printRow(6))    
    