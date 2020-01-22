# 도시 왕복하기 1
# https://www.acmicpc.net/problem/17412
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline
from collections import deque

n, p = map(int, input().split(' '))
nn = n - 1

c = [[0] * (2*n+1) for j in range(2*n+1)]
f = [[0] * (2*n+1) for j in range(2*n+1)]
edges = {}
for i in range(1, 2*n+1):
    edges[i] = []

for xxx in range(p):
    temp = tuple(map(int, rl().rstrip().split(' ')))
    s = temp[0]
    e = temp[1]
    if c[e][s] == 1:
        nn += 1
        c[s][nn] = 1
        c[nn][e] = 1
        edges[s].append(nn)
        edges[nn].append(e)
    else:
        c[s][e] = 1
        edges[s].append(e)
        edges[e].append(s)
for i in range(1, 2*n+1):
    c[i][i] = 1

source = 1
sink = 2
total = 0

while True:
    parents = [-1] * (2*n+1)

    q = deque()
    q.append(source)
    parents[source] = source
    while q and parents[sink]==-1:
        cur = q.popleft()
        for nex in edges[cur]:
            if c[cur][nex] - f[cur][nex] > 0 and parents[nex] == -1:
                parents[nex] = cur
                q.append(nex)

    if parents[sink] == -1:
        break

    flow = float('inf')
    cur = sink
    while cur != source:
        flow = min(flow, c[parents[cur]][cur] - f[parents[cur]][cur])
        cur = parents[cur]

    cur = sink
    while cur != source:
        f[parents[cur]][cur] += flow
        f[cur][parents[cur]] -= flow
        cur = parents[cur]
    total += flow
print(total)