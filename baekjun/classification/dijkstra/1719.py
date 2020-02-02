# 택배
# https://www.acmicpc.net/problem/1719
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline
from heapq import heappop, heappush

n, m = map(int, input().split(' '))
adj = {}
for i in range(1, n+1):
    adj[i] = {}
ans = [[-1] * (n+1) for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, rl().rstrip().split(' '))
    adj[u][v] = w
    adj[v][u] = w
    ans[u][v] = v
    ans[v][u] = u

pq = []
for start in range(1, n+1):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    heappush(pq, (0, start))
    while pq:
        cur = heappop(pq)
        cost = cur[0]
        here = cur[1]

        for there in adj[here]:
            nextCost = cost + adj[here][there]
            if nextCost < dist[there]:
                dist[there] = nextCost
                if here == start:
                    ans[start][there] = there
                else:
                    ans[start][there] = ans[start][here]
                heappush(pq, (nextCost, there))
for i in range(1, n+1):
    for j in range(1, n+1):
        if ans[i][j] == -1:
            print('-', end=' ')
        else:
            print(ans[i][j], end=' ')
    print('')