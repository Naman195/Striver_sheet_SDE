m = 3
n = 7

def uniquePath(m, n):
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    return solve(0,0, m, n, dp)

def solve(row, col, m, n, dp):
    if row == m-1 and col == n-1:
        return 1
    if row > m-1 or col > n-1:
        return 0
    
    if dp[row][col] != -1:
        return dp[row][col]
    
    right = solve(row, col+1, m, n, dp)
    down = solve(row+1, col, m, n, dp)
    dp[row][col] = right + down
    return dp[row][col]
print(uniquePath(m,n))