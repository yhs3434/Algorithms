# 2xn 타일링
# https://www.acmicpc.net/problem/11726

n = int(input())

if n<3:
    print(n)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    print(dp[-1])