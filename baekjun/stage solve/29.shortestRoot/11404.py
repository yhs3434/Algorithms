# 플로이드
# https://www.acmicpc.net/problem/11404
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, rl().rstrip().split(' '))
    dist[u][v] = min(w, dist[u][v])
for i in range(1, n+1):
    dist[i][i] = 0

update = True
while update:
    update = False
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    update = True

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print('')