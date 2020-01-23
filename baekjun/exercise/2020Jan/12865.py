# 평범한 배낭
# https://www.acmicpc.net/problem/12865
# https://github.com/yhs3434

n, k = map(int, input().split(' '))
things = []
for xxx in range(n):
    things.append(tuple(map(int, input().split(' '))))
things = [(0, 0)] + things
things.sort()

dp = [[0] * (k+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        val = 0
        if j - things[i][0] >= 0:
            val = dp[i-1][j - things[i][0]] + things[i][1]
        dp[i][j] = max(val, dp[i-1][j])
print(dp[-1][-1])