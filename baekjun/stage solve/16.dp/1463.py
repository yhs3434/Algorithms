# 1로 만들기
# https://www.acmicpc.net/problem/1463

def solution(n):
    answer = 0

    if n <= 3:
        if n == 1:
            return 0
        return 1
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n+1):
        vals = []
        if i%3 == 0:
            vals.append(dp[i//3] + 1)
        if i%2 == 0:
            vals.append(dp[i//2] + 1)
        vals.append(dp[i-1] + 1)
        dp[i] = min(vals)
    answer = dp[-1]
    return answer

n = int(input())
print(solution(n))