# 숨바꼭질
# https://www.acmicpc.net/problem/1697
# https://github.com/yhs3434

from collections import deque

n, k = map(int, input().split(' '))
q = deque()
q.append((n, 0))
answer = 0
#visited = [False] * 300000
#visited[n] = True
_SIZE_ = 400000
visited = [False] * _SIZE_
visited[n] = True
while q:
    cur = q.popleft()
    p = cur[0]
    cCnt = cur[1]

    if p == k:
        answer = cCnt
        break

    if -((_SIZE_)//2-1)<=(p-1)<=((_SIZE_)//2-1) and not visited[p-1]:
        q.append((p-1, cCnt+1))
        visited[p-1] = True
    if -((_SIZE_)//2-1)<=(p+1)<=((_SIZE_)//2-1) and not visited[p+1]:
        q.append((p + 1, cCnt + 1))
        visited[p+1] = True
    if -((_SIZE_)//2-1)<=p*2<=((_SIZE_)//2-1) and not visited[p*2]:
        q.append((2*p, cCnt + 1))
        visited[p*2] = True

print(answer)