# 토마토
# https://www.acmicpc.net/problem/7576
# https://github.com/yhs3434/Algorithms

from collections import deque
import sys
rl = sys.stdin.readline

def isRight2(board):
    return isRightRow(0, len(board)-1, board)

def isRightRow(up, down, board):
    if up == down:
        if 0 in board[up]:
            return False
        else:
            return True

    mid = (up + down) // 2
    if not isRightRow(up, mid, board):
        return False
    if not isRightRow(mid+1, down, board):
        return False
    return True


m, n = map(int, rl().rstrip().split(' '))
board = []
tomatos = []
cntZero = 0
for i in range(n):
    row = list(map(int, rl().rstrip().split(' ')))
    board.append(row)
    cntZero += row.count(0)
    for j in range(m):
        if row[j] == 1:
            tomatos.append((i, j))
if cntZero == 0:
    print(0)
else:
    answer = float('inf')
    q = deque()
    for tomato in tomatos:
        q.append((tomato, 1))
    while q:
        cur = q.popleft()
        r = cur[0][0]
        c = cur[0][1]
        cCnt = cur[1]

        if r-1 >= 0 and board[r-1][c] == 0:
            q.append(((r-1, c), cCnt+1))
            board[r-1][c] = 1
            cntZero -= 1

        if c+1 < m and board[r][c+1] == 0:
            q.append(((r, c+1), cCnt+1))
            board[r][c+1] = 1
            cntZero -= 1
        if r+1 < n and board[r+1][c] == 0:
            q.append(((r+1, c), cCnt+1))
            board[r+1][c] = 1
            cntZero -= 1
        if c-1 >= 0 and board[r][c-1] == 0:
            q.append(((r, c-1), cCnt+1))
            board[r][c-1] = 1
            cntZero -= 1

        if cntZero == 0:
            if cCnt < answer:
                answer = cCnt

    if cntZero==0:
        print(answer)
    else:
        print(-1)