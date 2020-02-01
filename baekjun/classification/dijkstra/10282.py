# 해킹
# https://www.acmicpc.net/problem/10282
# https://github.com/yhs3434/Algorithms

from heapq import heappop, heappush

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split(' '))
    adj = {}
    for i in range(1, n+1):
        adj[i] = {}
    for __ in range(d):
        a, b, s = map(int, input().split(' '))
        adj[b][a] = s
    dist = [float('inf')] * (n+1)
    dist[c] = 0
    pq = []
    heappush(pq, (0, c))
    while pq:
        cur = heappop(pq)
        cost = cur[0]
        here = cur[1]

        for there in adj[here]:
            nextDist = cost + adj[here][there]
            if nextDist < dist[there]:
                dist[there] = nextDist
                heappush(pq, (nextDist, there))

    for i in range(len(dist)):
        if dist[i] == float('inf'):
            dist[i] = -1
    print(len(dist)-dist.count(-1), max(dist))