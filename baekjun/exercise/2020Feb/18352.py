# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352
# https://github.com/yhs3434/Algorithms

from heapq import heappush, heappop

n, m, k, x = map(int, input().split(' '))

adj = {}
for i in range(1, n+1):
    adj[i] = {}
for _ in range(m):
    u, v = map(int, input().split(' '))
    adj[u][v] = 1

pq = []
dist = [float('inf')] * (n+1)
dist[x] = 0
heappush(pq, (0, x))

while pq:
    cur = heappop(pq)
    cost = cur[0]
    here = cur[1]

    for there in adj[here]:
        nextDist = cost + 1
        if nextDist < dist[there]:
            dist[there] = nextDist
            heappush(pq, (nextDist, there))

if dist.count(k) == 0:
    print(-1)
else:
    for i in range(1, n+1):
        if dist[i] == k:
            print(i)