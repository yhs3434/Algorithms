import sys
sys.stdin = open('9input/in5.txt', 'r')
n, m = map(int,input().split(' '))
arr = []
for i in range(n):
    arr.append(list(map(int, input().split(' '))))

dp = [0 for i in range(m+1)]

for i in range(1, len(dp)):
    for j in range(len(arr)):
        weight = arr[j][0]
        price = arr[j][1]

        if i - weight >= 0:
            dp[i] = max(dp[i - weight] + price, dp[i])

print(dp[-1])