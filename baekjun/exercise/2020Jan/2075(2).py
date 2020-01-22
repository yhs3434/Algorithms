# n번째 큰 수
# https://www.acmicpc.net/problem/2075
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline
from heapq import heappush, heappop

pq = []
n = int(rl().rstrip())
for xxx in range(n):
    row = list(map(int, rl().rstrip().split(' ')))
    for c in row:
        heappush(pq, c)
    cLen = len(pq)
    while cLen > n:
        heappop(pq)
        cLen -= 1
print(heappop(pq))