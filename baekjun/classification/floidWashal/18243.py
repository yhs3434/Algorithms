# Small World Network
# https://www.acmicpc.net/problem/18243
# https://github.com/yhs3434/Algorithms

N, K = map(int, input().split(' '))
dist = [[float('inf')] * (N+1) for _ in range(N+1)]
for _ in range(K):
    u, v = map(int, input().split(' '))
    dist[u][v] = 1
    dist[v][u] = 1
for i in range(1, N+1):
    dist[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
flag = True
for i in range(1, N+1):
    if flag:
        for j in range(1, N+1):
            if dist[i][j] > 6:
                flag = False
                break

if not flag:
    print("Big World!")
else:
    print("Small World!")