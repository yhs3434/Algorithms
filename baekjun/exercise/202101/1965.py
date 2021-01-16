n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(1, n+1):
    maxCnt = 1
    for j in range(1, i):
        if arr[j] < arr[i]:
            maxCnt = max(maxCnt, dp[j]+1)
    dp[i] = max(dp[i], maxCnt)
print(max(dp))