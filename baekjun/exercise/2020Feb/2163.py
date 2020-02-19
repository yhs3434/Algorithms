# 초콜릿 자르기
# https://www.acmicpc.net/problem/2163
# https://github.com/yhs3434/Algorithms

n, m = map(int, input().split(' '))
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, m+1):
    dp[1][i] = i-1

for i in range(2, n+1):
    for j in range(1,m+1):
        i1 = 1
        i2 = i - 1
        dp[i][j] = dp[i1][j] + dp[i2][j] + 1
print(dp[-1][-1])