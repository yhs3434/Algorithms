# 숨바꼭질
# https://www.acmicpc.net/problem/6118
# https://github.com/yhs3434/Algorithms

from heapq import heappush, heappop

n, m = map(int, input().split(' '))
adj = {}
for i in range(1, n+1):
    adj[i] = {}
for _ in range(m):
    u, v = map(int, input().split(' '))
    adj[u][v] = 1
    adj[v][u] = 1

dist = [float('inf')] * (n+1)
dist[1] = 0

pq = []
heappush(pq, (0, 1))
while pq:
    cur = heappop(pq)
    cost = cur[0]
    here = cur[1]

    for there in adj[here]:
        nextDist = cost + adj[here][there]
        if nextDist < dist[there]:
            dist[there] = nextDist
            heappush(pq, (nextDist, there))
maxVal = 0
maxIdx = 0
for i in range(2, n+1):
    val = dist[i]
    if val > maxVal:
        maxVal = val
        maxIdx = i
print(maxIdx, maxVal, dist.count(maxVal))