# 가장 긴 바이토닉 부분 수열
# https://www.acmicpc.net/problem/11054

def solution(n, arr):
    dp = [[0 for i in range(n)] for j in range(2)]
    dp[0][0] = 1
    dp[1][0] = 1
    for i in range(1, n):
        maxVals = []
        minVals = []
        for j in range(i):
            if arr[j] < arr[i]:
                maxVals.append(dp[0][j])
            if arr[j] > arr[i]:
                minVals.append(dp[0][j])
                minVals.append(dp[1][j])
        dp[0][i] = max(maxVals) + 1 if maxVals else 1
        dp[1][i] = max(minVals) + 1 if minVals else 1
    answer = max(max(dp[0]), max(dp[1]))
    return answer

n = int(input())
arr = list(map(int, input().split(' ')))
print(solution(n, arr))