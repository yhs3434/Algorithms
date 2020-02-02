# Line Friends (Small)
# https://www.acmicpc.net/problem/14588
# https://github.com/yhs3434/Algorithms

N = int(input())
lines = []
for i in range(N):
    u, v = map(int ,input().split(' '))
    lines.append((u, v, i))
lines.sort()
dist = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    right = lines[i][1]
    for j in range(i+1, N):
        if lines[j][0] <= right:
            dist[lines[i][2]][lines[j][2]] = 1
            dist[lines[j][2]][lines[i][2]] = 1
for i in range(N):
    dist[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split(' '))
    if dist[a-1][b-1] == float('inf'):
        print(-1)
    else:
        print(dist[a-1][b-1])