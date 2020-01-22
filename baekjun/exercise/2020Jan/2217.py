# 로프
# https://www.acmicpc.net/problem/2217
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline

n = int(input())
ropes = []
for xxx in range(n):
    ropes.append(int(rl().rstrip()))
ropes.sort(reverse=True)
dp = [0] * n
dp[0] = ropes[0]
for i in range(1, n):
    dp[i] = max(dp[i-1], ropes[i]*(i+1))
print(dp[-1])