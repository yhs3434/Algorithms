# 바이러스
# https://www.acmicpc.net/problem/2606

import queue

n = int(input())
m = int(input())
links = {}
computers = [i for i in range(1, n+1)]

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

visited = [1]
q = queue.Queue()
q.put(1)
while not q.empty():
    cCom = q.get()
    for nCom in links[cCom]:
        if nCom not in visited:
            q.put(nCom)
            visited.append(nCom)
print(len(visited)-1)