# 미확인 도착지
# https://www.acmicpc.net/problem/9370
# https://github.com/yhs3434/Algorithms

from heapq import heappush, heappop
from collections import deque
import sys
rl = sys.stdin.readline

def getDist(n, weight, u):
    pq = []
    dist = [float('inf')] * (n + 1)
    dist[u] = 0
    heappush(pq, (0, u))
    while pq:
        cur = heappop(pq)
        cost = cur[0]
        here = cur[1]

        for there in weight[here]:
            nextDist = cost + weight[here][there]
            if nextDist < dist[there]:
                dist[there] = nextDist
                heappush(pq, (nextDist, there))
    return dist

T = int(input())
for _ in range(T):
    n, m, t = map(int, rl().rstrip().split(' '))
    s, g, h = map(int, rl().rstrip().split(' '))

    weight = {}
    for i in range(1, n+1):
        weight[i] = {}
    for __ in range(m):
        u, v, w = map(int, rl().rstrip().split(' '))
        if (u == g and v == h) or (u == h and v == g):
            if v not in weight[u]:
                weight[u][v] = 2*w - 1
            else:
                weight[u][v] = min(2*w -1, weight[u][v])
            if u not in weight[v]:
                weight[v][u] = 2*w - 1
            else:
                weight[v][u] = min(2*w - 1, weight[v][u])
        else:
            if v not in weight[u]:
                weight[u][v] = 2*w
            else:
                weight[u][v] = min(2*w, weight[u][v])
            if u not in weight[v]:
                weight[v][u] = 2*w
            else:
                weight[v][u] = min(2*w, weight[v][u])

    dests = []
    for __ in range(t):
        x = int(rl().rstrip())
        dests.append(x)
    dests.sort()
    dist = getDist(n, weight, s)
    for dest in dests:
        if dist[dest] % 2 == 1:
            print(dest, end=' ')
    print('')