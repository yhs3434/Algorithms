# LCS
# https://www.acmicpc.net/problem/9251

import numpy as np
import sys
sys.setrecursionlimit(10**6)

def solution(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for i in range(m)] for j in range(n)]

    if s1[0] == s2[0]:
        dp[0][0] = 1
    for j in range(1, m):
        if s1[0] == s2[j]:
            dp[0][j] = max(1, dp[0][j-1])
        else:
            dp[0][j] = dp[0][j-1]
    for i in range(1, n):
        if s1[i] == s2[0]:
            dp[i][0] = max(1, dp[i-1][0])
        else:
            dp[i][0] = dp[i-1][0]
        for j in range(1, m):
            if s1[i] == s2[j]:
                dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

str1 = input()
str2 = input()
print(solution(str1, str2))