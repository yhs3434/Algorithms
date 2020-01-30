# 결혼식
# https://www.acmicpc.net/problem/5567
# https://github.com/yhs3434/Algorithms

from collections import deque

n = int(input())
m = int(input())

adj = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split(' '))
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n+1)
q = deque()
q.append((1, 0))
answer = []
visited[1] = True
while q:
    cur = q.popleft()
    here = cur[0]
    cCnt = cur[1]

    if cCnt == 2:
        continue

    for there in adj[here]:
        if not visited[there]:
            visited[there] = True
            answer.append(there)
            q.append((there, cCnt+1))

print(len(answer))