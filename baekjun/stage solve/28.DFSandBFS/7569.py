# 토마토
# https://www.acmicpc.net/problem/7569
# https://github.com/yhs3434/Algorithms

from collections import deque
nhrc = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, -1], [0, 0, 1]]

m, n, h = map(int,input().split(' '))

zeroCnt = 0
board = []
for xxx in range(h):
    floor = []
    for yyy in range(n):
        inp = list(map(int, input().split(' ')))
        zeroCnt += inp.count(0)
        floor.append(inp)
    board.append(floor)
flag = False
if zeroCnt == 0:
    flag = True

q = deque()
answer = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j] == 1:
                q.append((k, i, j, 0))
while q:
    cur = q.popleft()
    l = cur[0]
    r = cur[1]
    c = cur[2]
    cCnt = cur[3]
    for a in range(len(nhrc)):
        xx = nhrc[a]
        nl = xx[0] + l
        nr = xx[1] + r
        nc = xx[2] + c

        if 0 <= nl < h and 0<= nr < n and 0 <= nc < m:
            if board[nl][nr][nc] == 0:
                board[nl][nr][nc] = 1
                q.append((nl, nr, nc, cCnt+1))
                zeroCnt -= 1

    if zeroCnt == 0:
        answer = cCnt + 1
        break
if zeroCnt > 0:
    print(-1)
else:
    if flag:
        print(0)
    else:
        print(answer)