# 특정한 최단 경로
# https://www.acmicpc.net/problem/1504
# https://github.com/yhs3434/Algorithms

from heapq import heappush, heappop
from collections import deque

def getDist(N, weight, u, v):
    dist = [float('inf')] * (N + 1)
    dist[u] = 0

    pq = []
    heappush(pq, (0, u))
    while pq:
        cur = heappop(pq)
        cost = cur[0]
        here = cur[1]

        if cost > dist[here]:
            continue

        for there in weight[here]:
            nextDist = cost + weight[here][there]
            if nextDist < dist[there]:
                dist[there] = nextDist
                heappush(pq, (nextDist, there))
    return dist[v]

N, E = map(int, input().split(' '))

weight = {}

for i in range(1, N+1):
    weight[i] = {}
for i in range(E):
    a, b, w = map(int, input().split(' '))
    if b not in weight[a]:
        weight[a][b] = w
    else:
        weight[a][b] = min(w, weight[a][b])
    if a not in weight[b]:
        weight[b][a] = w
    else:
        weight[b][a] = min(w, weight[b][a])
v1, v2 = map(int, input().split(' '))

answer1, answer2 = 0, 0

answer1 += getDist(N, weight, 1, v1)
answer1 += getDist(N, weight, v1, v2)
answer1 += getDist(N, weight, v2, N)

answer2 += getDist(N, weight, 1, v2)
answer2 += getDist(N, weight, v2, v1)
answer2 += getDist(N, weight, v1, N)

answer = min(answer1, answer2)
if answer == float('inf'):
    print(-1)
else:
    print(answer)