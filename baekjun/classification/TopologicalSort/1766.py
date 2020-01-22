# 문제집
# https://www.acmicpc.net/problem/1766
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline
from collections import deque
from heapq import heappush, heappop

tshash = {}
n, m = map(int, input().split(' '))
for i in range(1, n+1):
    tshash[i] = {
        'ind': 0,
        'nex': []
    }
for xxx in range(m):
    s, e = map(int, rl().rstrip().split(' '))
    tshash[s]['nex'].append(e)
    tshash[e]['ind'] += 1


heapp = []
for i in range(1, n+1):
    if tshash[i]['ind'] == 0:
        heappush(heapp, i)

answer = []
while heapp:
    cur = heappop(heapp)
    answer.append(cur)

    for nex in tshash[cur]['nex']:
        tshash[nex]['ind'] -= 1
        if tshash[nex]['ind'] == 0:
            heappush(heapp, nex)
for a in answer:
    print(a, end=' ')