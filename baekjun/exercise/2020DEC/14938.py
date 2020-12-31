import numpy as np

n, m, r = map(int, input().split())

adj = {}
for i in range(1, n+1):
    adj[i] = {}
dp = [[float('inf') for i in range(n+1)] for j in range(n+1)]
for i in range(1, n+1):
    dp[i][i] = 0

itemNums = list(map(int, input().split()))
for _ in range(r):
    a, b, l = map(int, input().split())
    adj[a][b] = l
    adj[b][a] = l
    dp[a][b] = min(dp[a][b], l)
    dp[b][a] = min(dp[b][a], l)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

maxNumItem = 0

for i in range(1, n+1):
    numItem = 0
    for j in range(1, n+1):
        if dp[i][j] <= m:
            numItem += itemNums[j-1]
    maxNumItem = max(maxNumItem, numItem)

print(maxNumItem)