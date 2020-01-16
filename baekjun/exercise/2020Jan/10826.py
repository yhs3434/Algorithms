# 피보나치 수 4
# https://www.acmicpc.net/problem/10826

def fivo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[-1]

n = int(input())
print(fivo(n))