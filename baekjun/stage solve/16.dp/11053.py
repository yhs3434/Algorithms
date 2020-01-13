# 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

def solution(n, arr):
    answer = 0

    dp = [0 for i in range(n)]
    dp[0] = 1
    for i in range(1, n):
        vals = []
        for j in range(i):
            if arr[j] < arr[i]:
                vals.append(dp[j])
        if not vals:
            dp[i] = 1
        else:
            dp[i] = max(vals) + 1

    answer = max(dp)

    return answer

n = int(input())
arr = list(map(int, input().split(' ')))
print(solution(n, arr))