# DFS와 BFS
# https://www.acmicpc.net/problem/1260

import queue

n, m, v = map(int, input().split(' '))
links = {}
for i in range(1, n+1):
    links[i] = []
for xxx in range(m):
    a, b = map(int, input().split(' '))
    if a not in links:
        links[a] = [b]
    else:
        links[a].append(b)
    if b not in links:
        links[b] = [a]
    else:
        links[b].append(a)

for key in links:
    links[key].sort(reverse=True)
st = []
q = queue.Queue()

visitedSt = []
st.append(v)
while st:
    cur = st.pop()
    if cur not in visitedSt:
        visitedSt.append(cur)
    for nex in links[cur]:
        if nex not in visitedSt:
            st.append(nex)

for key in links:
    links[key].reverse()

visitedQ = [v]
q.put(v)
while not q.empty():
    cur = q.get()
    for nex in links[cur]:
        if nex not in visitedQ:
            q.put(nex)
            visitedQ.append(nex)

for vv in visitedSt:
    print(vv, end=' ')
print('')
for vv in visitedQ:
    print(vv, end=' ')
