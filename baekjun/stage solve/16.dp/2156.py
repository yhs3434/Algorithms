# 포도주 시식
# https://www.acmicpc.net/problem/2156

def solution(wines):
    answer = 0
    n = len(wines)
    if n==1:
        return wines[0]
    if n==2:
        return wines[0] + wines[1]
    dp = [[0 for i in range(n)] for j in range(3)]
    dp[0][0] = 0
    dp[1][0] = wines[0]
    dp[2][0] = 0
    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
        dp[1][i] = dp[0][i-1] + wines[i]
        dp[2][i] = dp[1][i-1] + wines[i]
    answer = max(dp[0][-1], dp[1][-1], dp[2][-1])
    return answer

n = int(input())
wines = []
for xxx in range(n):
    wines.append(int(input()))
print(solution(wines))