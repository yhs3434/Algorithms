N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N+1):
    for j in range(1, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])
    dp[i] = max(arr[i], dp[i])
print(max(dp))