# 스도쿠
# https://www.acmicpc.net/problem/2580

import queue

def solution(board):
    answer = []
    newBoard = []
    for b in board:
        newBoard.extend(b)
    #q = queue.Queue()
    #q.put((0, 0, board[:]))
    st = []
    st.append((0, 0, newBoard[:]))
    while st:
        cur = st.pop()
        r = cur[0]
        c = cur[1]
        cBoard = cur[2]

        while cBoard[r*9+c] != 0:
            c = (c+1)%9
            if c == 0:
                r += 1
            if r == 9:
                break
        if r==9:
            return cBoard
        else:
            avails = availRight(r, c, cBoard)
            for avail in avails:
                rBoard = cBoard[:]
                rBoard[r*9 + c] = avail
                st.append((r, c, rBoard))

    return answer

def availRight(r, c, board):
    idxs = [True for i in range(9)]
    for i in range(9):
        if board[i*9 + c] > 0:
            idxs[board[i*9+c]-1] = False
        if board[r*9 + i] > 0:
            idxs[board[r*9+i]-1] = False
    sr = r//3*3
    sc = c//3*3
    for i in range(3):
        for j in range(3):
            if board[(sr+i)*9 + sc+j] > 0:
                idxs[board[(sr+i)*9 + sc+j]-1] = False
    ret = []
    for i in range(9):
        if idxs[i]:
            ret.append(i+1)
    return ret

board = []
for xxx in range(9):
    board.append(list(map(int, input().split(' '))))
cBoard = solution(board)
for i in range(9):
    for j in range(9):
        print(cBoard[i*9 + j], end=' ')
    print('')