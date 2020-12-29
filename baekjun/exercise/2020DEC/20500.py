import sys
read = sys.stdin.readline

N = int(read())

dp = [0] * (N+1)

for i in range(2, N+1):
    if i % 2 == 0:
        dp[i] = dp[i-1] * 2 + 1
    else:
        dp[i] = dp[i-1] * 2 - 1

print(dp[N]%1000000007)