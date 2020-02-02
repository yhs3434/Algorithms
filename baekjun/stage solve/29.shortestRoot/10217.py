# KCM Travel
# https://www.acmicpc.net/problem/10217
# https://github.com/yhs3434/Algorithms

from heapq import heappop, heappush
import sys
rl = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = map(int, rl().rstrip().split(' '))
    price = {}
    adj = {}
    for i in range(N+1):
        price[i] = {}
        adj[i] = {}
    for _ in range(K):
        u, v, c, d = map(int, rl().rstrip().split(' '))
        price[u][v] = c
        adj[u][v] = d
    dist = [[float('inf')] * (M+1) for _ in range(N+1)]
    dist[1][0] = 0

    pq = []
    heappush(pq, (0, 1, 0)) # (here, price, cost)

    while pq:
        cur = heappop(pq)
        here = cur[1]
        cPrice = cur[2]
        cost = cur[0]

        for there in adj[here]:
            nextDist = cost + adj[here][there]
            nextPrice = cPrice + price[here][there]
            if nextPrice <= M:
                if nextDist < dist[there][nextPrice]:
                    dist[there][nextPrice] = nextDist
                    heappush(pq, (nextDist, there, nextPrice))

    answer = min(dist[N])
    if answer == float('inf'):
        print('Poor KCM')
    else:
        print(answer)