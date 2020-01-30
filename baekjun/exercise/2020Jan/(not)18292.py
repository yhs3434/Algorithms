# NM과 K (2)
# https://www.acmicpc.net/problem/18292
# https://github.com/yhs3434/Algorithms

from collections import deque
import copy

N, M, K = map(int, input().split(' '))
total = N*M
board = []
for _ in range(N):
    board.append(list(map(int, input().split(' '))))

answer = -float('inf')
q = deque()

visited = {}

for r in range(N):
    for c in range(M):
        newVisited = copy.deepcopy(visited)
        if r in newVisited:
            newVisited[r][c] = True
        else:
            newVisited[r] = {}
            newVisited[r][c] = True
        q.append((r, c, 1, newVisited))

while q:
    cur = q.popleft()
    r = cur[0]
    c = cur[1]
    cCnt = cur[2]
    cVisited = cur[3]

    if cCnt == K:
        val = 0
        for i in range(N):
            if (total - (i-1)*M) < 2*K:
                break
            for j in range(M):
                if i in cVisited and j in cVisited[i]:
                    val += board[i][j]
        if val > answer:
            answer = val
    else:
        for i in range(r, N):
            for j in range(M):
                if i==r:
                    if j<=c:
                        continue
                else:
                    if (i-1) in cVisited and j in cVisited[i-1]:
                        continue
                    elif (i+1) in cVisited and j in cVisited[i+1]:
                        continue
                    elif i in cVisited and (j-1) in cVisited[i]:
                        continue
                    elif i in cVisited and (j+1) in cVisited[i]:
                        continue
                    else:
                        newVisited = copy.deepcopy(cVisited)
                        if i in newVisited:
                            newVisited[i][j] = True
                        else:
                            newVisited[i] = {}
                            newVisited[i][j] = True
                        q.append((i, j, cCnt+1, newVisited))
print(answer)