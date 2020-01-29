# 최소비용 구하기
# https://www.acmicpc.net/problem/1916
# https://github.com/yhs3434/Algorithms

from heapq import heappop, heappush

n = int(input())
m = int(input())
weight = {}
dist = [float('inf')] * (n+1)
for i in range(1, n+1):
    weight[i] = {}

for _ in range(m):
    u, v, w = map(int, input().split(' '))
    if v not in weight[u]:
        weight[u][v] = w
    else:
        weight[u][v] = min(weight[u][v], w)

a, b = map(int, input().split(' '))

dist[a] = 0

pq = []
heappush(pq, (0, a))

while pq:
    cur = heappop(pq)
    cost = cur[0]
    here = cur[1]

    if dist[here] >= cost:
        for there in weight[here]:
            nextDist = cost + weight[here][there]
            if nextDist < dist[there]:
                dist[there] = nextDist
                heappush(pq, (nextDist, there))
print(dist[b])