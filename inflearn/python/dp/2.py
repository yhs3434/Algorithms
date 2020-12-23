import sys
sys.stdin = open('2.txt', 'r')
n = int(input())
arr = [0] + list(map(int, input().split(' ')))

dp = [1 for i in range(n+1)]

for i in range(2, len(dp)):
    for j in range(i-1, 0, -1):
        if arr[i] <= arr[j] or dp[i] > dp[j]:
            continue
        dp[i] = dp[j] + 1
print(dp)
print(max(dp))