# 파도반 수열
# https://www.acmicpc.net/problem/9461

def solution(n):
    answer = 0

    if n <= 3:
        return 1

    dp = [0 for i in range(n)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    i = 3
    while i < n:
        dp[i] = dp[i-3] + dp[i-2]
        i += 1
    answer = dp[-1]
    return answer

t = int(input())
for xxx in range(t):
    n = int(input())
    print(solution(n))