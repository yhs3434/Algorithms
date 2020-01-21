# ACM Craft
# https://www.acmicpc.net/problem/1005
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline
from collections import deque

def solution(n, k, times, edgeHash, w):
    q = deque()
    q.append((w, times[w]))
    dp = [0] * (n+1)
    #st = []
    #st.append((w, times[w]))
    dp[w] = times[w]
    while q:
        cur = q.popleft()
        cPos = cur[0]
        cPrice = cur[1]

        if cPos in edgeHash:
            for nPos in edgeHash[cPos]:
                if cPrice+times[nPos] > dp[nPos]:
                    q.append((nPos, cPrice + times[nPos]))
                    dp[nPos] = cPrice + times[nPos]
    return max(dp)

t = int(input())
for xxx in range(t):
    n, k = map(int, rl().rstrip().split(' '))
    times = [0] + list(map(int, rl().rstrip().split(' ')))
    edgeHash = {}
    for yyy in range(k):
        edge = tuple(map(int, rl().rstrip().split(' ')))
        s = edge[1]
        e = edge[0]
        if s not in edgeHash:
            edgeHash[s] = [e]
        else:
            edgeHash[s].append(e)
    w = int(rl().rstrip())
    print(solution(n, k, times, edgeHash, w))