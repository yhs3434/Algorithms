import sys
sys.stdin = open('13input/in5.txt', 'r')

N = int(input())

dp = [[float('inf') for i in range(N+1)] for j in range(N+1)]

while True:
    a, b = map(int, input().rstrip().split())
    if a == -1 and b == -1:
        break
    dp[a][b] = 1
    dp[b][a] = 1

for i in range(1, N+1):
    dp[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

scores = [float('inf')] * (N+1)
for i in range(1, N+1):
    arr = dp[i][1:]
    scores[i] = max(arr)
score = min(scores[1:])
people = []
for i in range(1, N+1):
    if scores[i] == score:
        people.append(i)

print(score, len(people))
print(people)