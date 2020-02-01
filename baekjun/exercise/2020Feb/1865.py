# 웜홀
# https://www.acmicpc.net/problem/1865
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, w = map(int, rl().rstrip().split(' '))
    adj = {}
    for i in range(1, n+1):
        adj[i] = {}
    for __ in range(m):
        s, e, t = map(int, rl().rstrip().split(' '))
        if e not in adj[s]:
            adj[s][e] = t
        else:
            adj[s][e] = min(t, adj[s][e])
        if s not in adj[e]:
            adj[e][s] = t
        else:
            adj[e][s] = min(t, adj[e][s])
    for __ in range(w):
        s, e, t = map(int, rl().rstrip().split(' '))
        if e not in adj[s]:
            adj[s][e] = -t
        else:
            adj[s][e] = min(-t, adj[s][e])
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    update = True
    cnt = 0
    while update and cnt < n:
        cnt += 1
        update = False
        for here in range(1, n+1):
            for there in adj[here]:
                nextDist = dist[here] + adj[here][there]
                if nextDist < dist[there]:
                    dist[there] = nextDist
                    update = True

    if cnt == n:
        print('YES')
    else:
        print('NO')