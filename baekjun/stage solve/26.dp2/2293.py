# 동전 1
# https://www.acmicpc.net/problem/2293
# https://github.com/yhs3434

import sys
rl = sys.stdin.readline

n, k = map(int, input().split(' '))
coins = []
coins.sort()
for i in range(n):
    coins.append(int(rl().rstrip()))
dp = [[0 for j in range(k+1)] for i in range(2)]

for j in range(k+1):
    dp[0][j] = 1 if j%coins[0]==0 else 0

for i in range(1, n):
    l = i
    i = i % 2
    for j in range(k+1):
        if i == 1:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i+1][j]
        if j - coins[l] >= 0:
            dp[i][j] += dp[i][j-coins[l]]
print(max(dp[0][-1], dp[-1][-1]))