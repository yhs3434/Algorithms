# 줄 세우기
# https://www.acmicpc.net/problem/2252
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

n, m = map(int, input().split(' '))
sehash = {}
st = []

def topologicalSort(cur, sehash, visited, st):
    for nex in sehash[cur]['bef']:
        if not visited[nex]:
            visited[nex] = True
            topologicalSort(nex, sehash, visited, st)
    st.append(cur)

for i in range(1, n+1):
    sehash[i] = {
        'bef': [],
        'nex': []
    }

for xxx in range(m):
    s, e = map(int, rl().rstrip().split(' '))
    sehash[s]['nex'].append(e)
    sehash[e]['bef'].append(s)

ends = []

visited = [False] * (n+1)
q = deque()
for i in range(1, n+1):
    if not visited[i]:
        q.append(i)
        visited[i] = True
        while q:
            cur = q.popleft()

            if len(sehash[cur]['nex']) == 0:
                ends.append(cur)
            else:
                for nex in sehash[cur]['nex']:
                    if not visited[nex]:
                        q.append(nex)
                        visited[nex] = True
visited = [False] * (n+1)
for end in ends:
    visited[end] = True
    topologicalSort(end, sehash, visited, st)
for ss in st:
    print(ss, end=' ')