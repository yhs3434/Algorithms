K = int(input())

dp = [0] * (K+1)
dp[1] = 1
for i in range(2, K+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[-2], dp[-1 ])