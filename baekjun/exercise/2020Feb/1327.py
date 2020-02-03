# 소트 게임
# https://www.acmicpc.net/problem/1327
# https://github.com/yhs3434/Algorithms

from collections import deque

N, K = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
target = sorted(arr)

answer = float('inf')
visited = {}
visited[str(arr)] = True

q = deque()
q.append((arr[:], 0))
while q:
    cur = q.popleft()
    cArr = cur[0]
    cCnt = cur[1]

    if cArr==target:
        answer = cCnt
        break

    for i in range(N-K+1):
        nArr = cArr[:]
        left = nArr[:i]
        mid = nArr[i:i+K]
        mid.reverse()
        right = nArr[i+K:]
        nArr = left + mid + right

        #print(cArr, nArr)
        if str(nArr) not in visited:
            visited[str(nArr)] = True
            q.append((nArr, cCnt+1))

if answer == float('inf'):
    print(-1)
else:
    print(answer)