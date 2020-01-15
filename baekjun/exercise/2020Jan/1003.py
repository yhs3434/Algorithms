# 피보나치 함수
# https://www.acmicpc.net/problem/1003

t = int(input())
dp = [[0 for i in range(41)] for j in range(2)]
dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1
for i in range(2):
    for j in range(2, 41):
        dp[i][j] = dp[i][j-1] + dp[i][j-2]

for xxx in range(t):
    n = int(input())
    print(dp[0][n], dp[1][n])