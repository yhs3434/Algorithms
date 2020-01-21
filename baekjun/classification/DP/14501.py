# 퇴사
# https://www.acmicpc.net/problem/14501
# https://github.com/yhs3434

import sys
rl = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split(' '))))
arr = [(0, 0)] + arr

dp = [0] * (n+2)
dp[n] = 0
for i in range(n, 0, -1):
    if arr[i][0] <= n-i+1:
        dp[i] = max(dp[i+1], arr[i][1] + dp[i+arr[i][0]])
    else:
        dp[i] = dp[i+1]
print(dp[1])