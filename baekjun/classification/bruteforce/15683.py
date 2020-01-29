# 감시
# https://www.acmicpc.net/problem/15683
# https://github.com/yhs3434/Algorithms

from collections import deque

def cntZero(board):
    cnt = 0
    for i in range(len(board)):
        cnt += board[i].count('0')
    return cnt

answer = []
n, m = map(int, input().split(' '))
board = []
for _ in range(n):
    board.append(input().split(' '))

cctvs = []
for i in range(n):
    for j in range(m):
        if 0 < int(board[i][j]) < 6:
            cctvs.append((i, j))

q = deque()

if cctvs:
    newBoard = [[board[i][j] for j in range(m)] for i in range(n)]
    nCctv = cctvs.pop()
    q.append((nCctv, cctvs[:], newBoard))
    while q:
        cur = q.popleft()
        r = cur[0][0]
        c = cur[0][1]
        cCctvs = cur[1]
        cBoard = cur[2]

        nCctv = -1
        if cCctvs:
            nCctv = cCctvs.pop()
        if board[r][c] == '1':
            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if r-i >= 0 and board[r-i][c] != '6':
                    if board[r-i][c] == '0':
                        newBoard[r-i][c] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if c + i < m and board[r][c+i] != '6':
                    if board[r][c+i] == '0':
                        newBoard[r][c+i] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if r + i < n and board[r+i][c] != '6':
                    if board[r+i][c] == '0':
                        newBoard[r+i][c] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if c - i >= 0 and board[r][c - i] != '6':
                    if board[r][c - i] == '0':
                        newBoard[r][c - i] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

        elif board[r][c] == '2':
            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if c - i >= 0 and board[r][c - i] != '6':
                    if board[r][c - i] == '0':
                        newBoard[r][c - i] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if c + i < m and board[r][c+i] != '6':
                    if board[r][c+i] == '0':
                        newBoard[r][c+i] = '#'
                else:
                    break
                i+=1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if r - i >= 0 and board[r-i][c] != '6':
                    if board[r-i][c] == '0':
                        newBoard[r-i][c] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if r + i < n and board[r+i][c] != '6':
                    if board[r+i][c] == '0':
                        newBoard[r+i][c] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

        elif board[r][c] == '3':
            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if r - i >= 0 and board[r-i][c] != '6':
                    if board[r-i][c] == '0':
                        newBoard[r-i][c] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if c + i < m and board[r][c + i] != '6':
                    if board[r][c + i] == '0':
                        newBoard[r][c + i] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if r + i < n and board[r + i][c] != '6':
                    if board[r + i][c] == '0':
                        newBoard[r + i][c] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if c + i < m and board[r][c + i] != '6':
                    if board[r][c + i] == '0':
                        newBoard[r][c + i] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if r + i < n and board[r + i][c] != '6':
                    if board[r + i][c] == '0':
                        newBoard[r + i][c] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if c - i >= 0 and board[r][c - i] != '6':
                    if board[r][c - i] == '0':
                        newBoard[r][c - i] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if r - i >= 0 and board[r - i][c] != '6':
                    if board[r - i][c] == '0':
                        newBoard[r - i][c] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if c - i >= 0 and board[r][c - i] != '6':
                    if board[r][c - i] == '0':
                        newBoard[r][c - i] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

        elif board[r][c] == '4':
            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if c - i >= 0 and board[r][c-i] != '6':
                    if board[r][c-i] == '0':
                        newBoard[r][c-i] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if r - i >= 0 and board[r-i][c] != '6':
                    if board[r-i][c] == '0':
                        newBoard[r-i][c] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if c + i < m and board[r][c + i] != '6':
                    if board[r][c + i] == '0':
                        newBoard[r][c + i] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if r + i < n and board[r+i][c] != '6':
                    if board[r+i][c] == '0':
                        newBoard[r+i][c] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if r - i >= 0 and board[r - i][c] != '6':
                    if board[r - i][c] == '0':
                        newBoard[r - i][c] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if c + i < m and board[r][c + i] != '6':
                    if board[r][c + i] == '0':
                        newBoard[r][c + i] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if r + i < n and board[r + i][c] != '6':
                    if board[r + i][c] == '0':
                        newBoard[r + i][c] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if c - i >= 0 and board[r][c-i] != '6':
                    if board[r][c-i] == '0':
                        newBoard[r][c-i] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if c + i < m and board[r][c + i] != '6':
                    if board[r][c + i] == '0':
                        newBoard[r][c + i] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if r + i < n and board[r + i][c] != '6':
                    if board[r + i][c] == '0':
                        newBoard[r + i][c] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if c - i >= 0 and board[r][c - i] != '6':
                    if board[r][c - i] == '0':
                        newBoard[r][c - i] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if r - i >= 0 and board[r-i][c] != '6':
                    if board[r-i][c] == '0':
                        newBoard[r-i][c] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

        elif board[r][c] == '5':
            newBoard = [[cBoard[i][j] for j in range(m)] for i in range(n)]
            i = 1
            while True:
                if r + i < n and board[r + i][c] != '6':
                    if board[r + i][c] == '0':
                        newBoard[r + i][c] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if c - i >= 0 and board[r][c - i] != '6':
                    if board[r][c - i] == '0':
                        newBoard[r][c - i] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if r - i >= 0 and board[r - i][c] != '6':
                    if board[r - i][c] == '0':
                        newBoard[r - i][c] = '#'
                else:
                    break
                i += 1
            i = 1
            while True:
                if c + i < m and board[r][c + i] != '6':
                    if board[r][c + i] == '0':
                        newBoard[r][c + i] = '#'
                else:
                    break
                i += 1
            if nCctv != -1:
                q.append((nCctv, cCctvs[:], newBoard))
            else:
                answer.append(cntZero(newBoard))

if answer:
    print(min(answer))
else:
    print(cntZero(board))