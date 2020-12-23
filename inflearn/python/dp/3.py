import sys
sys.stdin = open('3input/in5.txt', 'r')

n = int(input())

blocks = []
blocks.append([0, 0, 0])
for i in range(n):
    arr = list(map(int, input().split(' ')))
    blocks.append(arr)

blocks.sort(key=lambda block: block[2])
blocks.sort(key=lambda block: block[0])

dp = [0 for i in range(n+1)]
dp[1] = blocks[1][1]

for i in range(2, len(dp)):
    maxVal = 0
    for j in range(i-1, 0, -1):
        if blocks[i][2] > blocks[j][2]:
            if dp[j] > maxVal:
                maxVal = dp[j]
    dp[i] = maxVal + blocks[i][1]

print(max(dp))