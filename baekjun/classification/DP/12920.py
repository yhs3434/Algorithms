# 평범한 배낭 2
# https://www.acmicpc.net/problem/12920
# https://github.com/yhs3434

import sys
rl = sys.stdin.readline

n, m = map(int, rl().rstrip().split(' '))
things = []
for xxx in range(n):
    v, c, k = map(int, rl().rstrip().split(' '))
    mul = 1
    while k > 0:
        mm = min(mul, k)
        things.append((v*mm, c*mm))
        k -= mm
        mul = (mul << 1)
things.sort()

things = [(0, 0)] + things
dp = [[0] * (m+1) for i in range(len(things))]

for i in range(1, len(things)):
    for j in range(1, m+1):
        val = 0
        if j - things[i][0] >= 0:
            val = dp[i-1][j - things[i][0]] + things[i][1]
        dp[i][j] = max(dp[i-1][j], val)
print(dp[-1][-1])