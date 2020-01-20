# 파일 합치기
# https://www.acmicpc.net/problem/11066
# https://github.com/yhs3434

def solution(k, files):
    sumDp = [0] * (len(files)+1)
    for i in range(1, len(files)+1):
        sumDp[i] = sumDp[i-1] + files[i-1]
    dp = [[0 for j in range(len(files)+1)] for i in range(len(files)+1)]
    putDp(1, len(files),dp,sumDp)
    return dp[1][len(files)]

def putDp(i, j,dp, sumDp):
    if i==j:
        return 0
    if dp[i][j] > 0:
        return dp[i][j]
    val = float('inf')
    for k in range(i, j):
        val = min(val, putDp(i,k,dp,sumDp) + putDp(k+1,j,dp,sumDp))
    dp[i][j] = val + sumDp[j] - sumDp[i-1]
    return val + sumDp[j] - sumDp[i-1]

t = int(input())
for xxx in range(t):
    k = int(input())
    files = list(map(int, input().split(' ')))
    print(solution(k, files))