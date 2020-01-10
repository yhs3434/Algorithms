# 피보나치 수 2
# https://www.acmicpc.net/problem/2748

n = int(input())
dp = [0 for i in range(n+1)]
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[-1])