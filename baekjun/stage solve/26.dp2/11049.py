# 행렬 곱셈 순서
# https://www.acmicpc.net/problem/11049
# https://github.com/yhs3434

def solution(n, mat):
    dp = [[(0, [0, 0])]*n for i in range(n)]
    for i in range(n):
        dp[i][i] = (0, (mat[i]))
    putDp(0, n-1, dp, mat)

    return dp[0][n-1][0]

def putDp(l, r, dp, mat):
    if l == r:
        return dp[l][r]
    if dp[l][r][0] > 0:
        return dp[l][r]

    dp[l][r] = (float('inf'), [0, 0])
    for k in range(l, r):
        c1 = putDp(l, k, dp, mat)
        c2 = putDp(k+1, r, dp, mat)
        val = c1[1][0] * c1[1][1] * c2[1][1]
        dp[l][r] = min(dp[l][r], (c1[0]+c2[0]+val, (c1[1][0], c2[1][1])))
    return dp[l][r]

n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split(' '))))
print(solution(n, mat))