# 최소 힙
# https://www.acmicpc.net/problem/1927
# https://github.com/yhs3434

import sys
rl = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
cheap = []
for i in range(n):
    cur = int(rl().rstrip())
    if cur == 0:
        if not cheap:
            print(0)
        else:
            print(heappop(cheap))
    else:
        heappush(cheap, cur)