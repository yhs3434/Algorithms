# 운동
# https://www.acmicpc.net/problem/1956
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline

V, E = map(int, input().split(' '))
dist = [[float('inf')] * (V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, rl().rstrip().split(' '))
    dist[u][v] = min(w, dist[u][v])

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

minVal = float('inf')
for i in range(1, V+1):
    if dist[i][i] < minVal:
        minVal = dist[i][i]
if minVal == float('inf'):
    print(-1)
else:
    print(minVal)