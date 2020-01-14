# 제곱수의 합
# https://www.acmicpc.net/problem/1699

def solution(n):
    dp = [i for i in range(n+1)]
    for i in range(2, n+1):
        for j in range(1, int(i**(1/2))+1):
            dp[i] = min(dp[i], dp[i-j*j]+1)
    return dp[-1]

n = int(input())
print(solution(n))
