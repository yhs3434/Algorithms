# 01타일
# https://www.acmicpc.net/problem/1904

def solution(n):
    answer = 0
    if n == 1:
        return 1
    elif n == 2:
        return 2
    dp = [0 for i in range(3)]
    dp[0] = 1
    dp[1] = 2
    i = 2
    for x in range(n-2):
        dp[i] = dp[i-2] + dp[i-1]
        i = (i+1) % 3
    answer = dp[i-1]
    return answer%15746

n = int(input())
print(solution(n))