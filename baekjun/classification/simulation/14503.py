# 로봇 청소기
# https://www.acmicpc.net/problem/14503
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline
from collections import deque


nrcs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def getNrcsIdx(d):
    d -= 1
    if d < 0:
        d += 4
    return d

n, m = map(int, input().split(' '))
r1, c1, d1 = map(int, input().split(' '))
#r1 -= 1
#c1 -= 1

board = []
for xxx in range(n):
    inp = list(map(int, rl().rstrip().split(' ')))
    board.append(inp)

q = deque()
q.append((r1, c1, d1))

board[r1][c1] = 2
cnt = 1
while q:
    cur = q.popleft()
    r = cur[0]
    c = cur[1]
    d = cur[2]

    nd = d
    flag = False
    for i in range(4):
        nd = getNrcsIdx(nd)
        nr = nrcs[nd][0] + r
        nc = nrcs[nd][1] + c
        if board[nr][nc] == 0:
            flag = True
            break
    if flag:
        q.append((nr, nc, nd))
        board[nr][nc] = 2
        cnt += 1
    else:
        nd = d - 2
        if nd < 0:
            nd += 4
        nr = nrcs[nd][0] + r
        nc = nrcs[nd][1] + c
        if board[nr][nc] == 0 or board[nr][nc] == 2:
            q.append((nr, nc, d))
            #board[nr][nc] = 2
            #cnt += 1

print(cnt)