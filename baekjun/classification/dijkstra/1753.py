# 최단경로
# https://www.acmicpc.net/problem/1753
# https://github.com/yhs3434/Algorithms

from heapq import heappush, heappop

p, e = map(int, input().split(' '))
k = int(input())

weight = {}
distance = [float('inf')] * (p+1)
for i in range(1, p+1):
    weight[i] = {}

for _ in range(e):
    u, v, w = map(int, input().split(' '))
    #weight[u][v] = min(weight[u][v], w)
    if v not in weight[u]:
        weight[u][v] = w
    else:
        weight[u][v] = min(weight[u][v], w)

distance[k] = 0

pq = []
heappush(pq, (0, k))

while pq:
    cur = heappop(pq)
    cost = cur[0]
    here = cur[1]

    if distance[here] < cost:
        continue

    for there in weight[here]:
        nextDist = cost + weight[here][there]
        if distance[there] > nextDist:
            distance[there] = nextDist
            #for i in range(len(pq)-1, -1, -1):
            #    if pq[i][1] == there:
            #        del pq[i]
            heappush(pq, (nextDist, there))

for _ in range(1, p+1):
    if distance[_] == float('inf'):
        print('INF')
    else:
        print(distance[_])