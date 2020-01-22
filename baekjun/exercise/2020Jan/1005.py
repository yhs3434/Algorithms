# ACM Craft
# https://www.acmicpc.net/problem/1005
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline
from collections import deque

t = int(input())
for xxx in range(t):
    n, k = map(int, rl().rstrip().split(' '))
    times = [0] + list(map(int, rl().rstrip().split(' ')))
    eHash = {}
    for i in range(1, n+1):
        eHash[i] = []
    for yyy in range(k):
        s, e = map(int, rl().rstrip().split(' '))
        eHash[e].append(s)
    w = int(rl().rstrip())

    dp = [0] * (n+1)
    dp[w] = times[w]
    q = deque()
    q.append(w)

    while q:
        cur = q.popleft()

        for nex in eHash[cur]:
            if dp[nex] < dp[cur] + times[nex]:
                dp[nex] = dp[cur] + times[nex]
                q.append(nex)
    print(max(dp))