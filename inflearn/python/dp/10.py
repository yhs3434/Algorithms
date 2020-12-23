import sys
sys.stdin = open('10input/in5.txt', 'r')

N = int(input())
arr = list(map(int, input().rstrip().split()))
M = int(input())

dp = [float('inf') for i in range(M+1)]
dp[0] = 0
for i in range(1, len(dp)):
    for j in range(N):
        coin = arr[j]
        if i - coin >= 0:
            dp[i] = min(dp[i-coin] + 1, dp[i])
print(dp[-1])