# 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389
# https://github.com/yhs3434/Algorithms

n, m = map(int, input().split(' '))
dist = [[float('inf')] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split(' '))
    dist[u][v] = 1
    dist[v][u] = 1
for i in range(1, n+1):
    dist[i][i] = 0
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

minVal = float('inf')
minIdx = 0
for i in range(1, n+1):
    val = sum(dist[i][1:])
    if val < minVal:
        minVal = val
        minIdx = i
print(minIdx)