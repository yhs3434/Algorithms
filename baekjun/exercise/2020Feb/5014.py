# 스타트링크
# https://www.acmicpc.net/problem/5014
# https://github.com/yhs3434

from collections import deque

f, s, g, u, d = map(int, input().split(' '))

answer = 'use the stairs'

q = deque()
q.append((s, 0))
visited = [False] * (f+1)
visited[s] = True

while q:
    cur = q.popleft()
    here = cur[0]
    cCnt = cur[1]

    if here == g:
        answer = cCnt
        break

    if here + u <= f and not visited[here+u]:
        visited[here + u] = True
        q.append((here+u, cCnt+1))
    if here - d > 0 and not visited[here-d]:
        visited[here - d] = True
        q.append((here-d, cCnt + 1))
print(answer)