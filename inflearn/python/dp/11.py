import sys
sys.stdin = open('11input/in5.txt', 'r')

N, M = map(int, input().rstrip().split(' '))

arr = []
for i in range(N):
    arr.append(list(map(int, input().rstrip().split(' '))))

dp = [[0 for i in range(M+1)] for j in range(N+1)]

for i in range(N):
    problem = arr[i]
    score = problem[0]
    spend = problem[1]
    for j in range(spend, M+1):
        dp[i+1][j] = max(dp[i][j-spend] + score, dp[i][j])

print(dp[-1][-1])