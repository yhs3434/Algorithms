# 역사
# https://www.acmicpc.net/problem/1613
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline

n, k = map(int, input().split(' '))
dist = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(k):
    u, v = map(int, rl().rstrip().split(' '))
    dist[u][v] = 1
for i in range(1, n+1):
    dist[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

s = int(input())
for _ in range(s):
    x, y = map(int, rl().rstrip().split(' '))
    if dist[x][y] != float('inf'):
        print(-1)
    elif dist[y][x] != float('inf'):
        print(1)
    else:
        print(0)