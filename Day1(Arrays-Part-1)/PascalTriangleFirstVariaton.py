# Given row number and col number 

def nCr(row, col):
    res = 1
    for i in range(col): # run till col = 2 times
        res = res * (row - i) # res = 1 * (7-i) i =0
        res = res // (i+1)  # res = res // (i+1) => i = 1
    return res

print(nCr(6, 1))
