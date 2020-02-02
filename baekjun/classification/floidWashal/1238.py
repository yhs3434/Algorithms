# 파티
# https://www.acmicpc.net/problem/1238
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(N, adj, u, v):
    dist = [float('inf')] * (N+1)
    dist[u] = 0
    pq = []
    heappush(pq, (0, u))
    while pq:
        cur = heappop(pq)
        cost = cur[0]
        here = cur[1]

        for there in adj[here]:
            nextCost = cost + adj[here][there]
            if nextCost < dist[there]:
                dist[there] = nextCost
                heappush(pq, (nextCost, there))
    return dist[v]

N, M, X = map(int, rl().rstrip().split(' '))
adj = {}
for i in range(1, N+1):
    adj[i] = {}

for _ in range(M):
    u, v, t = map(int, rl().rstrip().split(' '))
    adj[u][v] = t

answer = 0
for i in range(1, N+1):
    time = dijkstra(N, adj, i, X) + dijkstra(N, adj, X, i)
    answer = max(answer, time)
print(answer)