# 3의 배수
# https://www.acmicpc.net/problem/16561
# https://github.com/yhs3434/Algorithms

from collections import deque

N = int(input())

n = N//3
n -= 2
dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = dp[i-1] + i
print(dp[-1])