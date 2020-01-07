# 쉬운 계단 수
# https://www.acmicpc.net/problem/10844

n = int(input())

dp = [[0 for j in range(10)] for i in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        sumVal = 0
        if j-1 >= 0:
            sumVal += dp[i-1][j-1]
        if j+1 < 10:
            sumVal += dp[i-1][j+1]
        dp[i][j] = sumVal
answer = sum(dp[-1])
print(answer%1000000000)