# Generations of Tribbles
# https://www.acmicpc.net/problem/9507
# https://github.com/yhs3434

import sys
rl = sys.stdin.readline

def solution(n):
    if n == 0:
        return 1
    elif n== 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

    return dp[-1]


t = int(input())
for xxx in range(t):
    n = int(rl().rstrip())
    print(solution(n))