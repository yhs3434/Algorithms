t = int(input())
from collections import deque

def getDist(prev, next):
    return abs(prev[0]- next[0]) + abs(prev[1] - next[1])

for _ in range(t):
    n = int(input())
    answer = 'happy'
    start = tuple(map(int, input().split()))
    cvstore = []
    for __ in range(n):
        cvstore.append(tuple(map(int, input().split())))
    end = tuple(map(int, input().split()))
    if getDist(start, end) <= 1000:
        print('happy')
        continue
    adj = {
        n: {},
        n+1: {}
    }
    for i in range(n):
        adj[i] = {}

    for i in range(n):
        adj[n][i] = getDist(start, cvstore[i])
        adj[i][n] = getDist(start, cvstore[i])
        adj[n+1][i] = getDist(end, cvstore[i])
        adj[i][n+1] = getDist(end, cvstore[i])
        for j in range(i):
            adj[i][j] = getDist(cvstore[i], cvstore[j])
            adj[j][i] = getDist(cvstore[i], cvstore[j])
    dp = [[float('inf')] * (n+2) for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if j in adj[i]:
                dp[i][j] = adj[i][j]
                dp[j][i] = adj[j][i]
    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    for i in range(len(dp)):
        if i >= n:
            break
        row = dp[i]
        cnt = 0
        for col in row:
            if col <= 1000:
                cnt += 1
        if cnt < 2:
            answer = 'sad'
            break
    for i in range(n, n+2):
        row = dp[i]
        cnt = 0
        for col in row:
            if col <= 1000:
                cnt += 1
        if cnt < 1:
            answer = 'sad'
            break
    print(answer)