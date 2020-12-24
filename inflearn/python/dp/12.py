import sys
sys.stdin = open('12input/in5.txt', 'r')
import numpy as np

N, M = map(int, input().rstrip().split())
adj = {}
dp = [[float('inf') for i in range(N+1)] for j in range(N+1)]
for i in range(1, N+1):
    dp[i][i] = 0
    adj[i] = {}
for i in range(M):
    a, b, p = map(int, input().rstrip().split())
    adj[a][b] = p
    dp[a][b] = p

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dist = dp[i][k] + dp[k][j]
            dp[i][j] = min(dist, dp[i][j])

print(np.array(dp))