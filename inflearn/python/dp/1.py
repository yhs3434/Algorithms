import sys
sys.stdin = open('1.txt', 'r')
n = int(input())

d = [-1 for i in range(n+1)]

d[1] = 1
d[2] = 2

def dfs(x, dp):
    if dp[x] > 0:
        return dp[x]

    dp[x] = dfs(x-1, dp) + dfs(x-2, dp)
    return dp[x]

print(dfs(n, d))