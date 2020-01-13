# 연속합
# https://www.acmicpc.net/problem/1912

def solution(n, arr):
    answer = 0

    dp = [0 for i in range(n)]
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(dp[i-1], 0) + arr[i]
    answer = max(dp)

    return answer

n = int(input())
arr = list(map(int, input().split(' ')))
print(solution(n, arr))