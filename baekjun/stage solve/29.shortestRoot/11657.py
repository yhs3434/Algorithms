# 타임머신
# https://www.acmicpc.net/problem/11657
# https://github.com/yhs3434/Algorithms

from collections import deque

N, M = map(int, input().split(' '))

weight = {}
for i in range(1, N+1):
    weight[i] = {}

for _ in range(M):
    u, v, w = map(int, input().split(' '))

    if v not in weight[u]:
        weight[u][v] = w
    else:
        weight[u][v] = min(weight[u][v], w)

dist = [float('inf')] * (N+1)
dist[1] = 0

loopCnt = 0
loopFlag = False

n = 0
while n <= N:
    for i in range(1, N+1):
        here = i
        for there in weight[here]:
            if dist[here] + weight[here][there] < dist[there]:
                if n == N:
                    loopFlag = True
                dist[there] = dist[here] + weight[here][there]
    n+=1

if loopFlag:
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])