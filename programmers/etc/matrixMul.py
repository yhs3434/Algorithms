# 최적의 행렬 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12942?language=python3

import numpy as np

def putDp(s, e, dp):
    if dp[s][e][1] != (0, 0):
        return dp[s][e]
    else:
        minVal = float('inf')
        minMat = (0, 0)
        for i in range(s, e):
            A = putDp(s, i, dp)
            B = putDp(i+1, e, dp)
            val = A[0] + B[0] + A[1][0] * A[1][1] * B[1][1]
            if val < minVal:
                minVal = val
                minMat = (A[1][0], B[1][1])
        dp[s][e][0] = minVal
        dp[s][e][1] = minMat
        return dp[s][e]

def solution(matrix_sizes):
    answer = 0
    lenn = len(matrix_sizes)
    dp = [[[0, (0, 0)] for _ in range(lenn)] for __ in range(lenn)]

    for i in range(lenn):
        dp[i][i][1] = (matrix_sizes[i][0], matrix_sizes[i][1])

    putDp(0, lenn-1, dp)
    answer = dp[0][lenn-1][0]
    return answer

print(solution([[5,3],[3,10],[10,6]]))