# 1767. [SW Test 샘플문제] 프로세서 연결하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf

import queue

def solution(board):
    answer = float('inf')
    #q = queue.Queue()
    #q.put((0, 0, board, 0))   # (행, board)

    stack = []
    stack.append((0, 0, board, 0))
    while stack:
        cur = stack.pop()
        r = cur[0]
        c = cur[1]
        cCnt = cur[3]

        if cCnt >= answer:
            continue
        if r==len(board):
            if cCnt < answer:
                answer = cCnt
        else:
            newR = r
            newC = (c + 1) % len(board)
            if newC == 0:
                newR += 1
            if isWrap(r, c, board):
                stack.append((newR, newC, cur[2], cCnt))
                continue

            if board[r][c] == 1:
                for i in range(4):
                    newBoard = [[cur[2][i][j] for j in range(len(board))] for i in range(len(board))]
                    wireCnt = putWire(r, c, newBoard, i)
                    if wireCnt >= 0:
                        stack.append((newR, newC, newBoard, cCnt+wireCnt))
            else:
                stack.append((newR, newC, cur[2], cCnt))
    return answer

def putWire(r, c, board, direction):
    cnt = 0
    if direction == 0:
        flag = True
        for i in range(r):
            if board[i][c] == 1:
                flag = False
                break
        if flag:
            for i in range(r):
                board[i][c] = 1
                cnt += 1
        else:
            return -1
    elif direction == 1:
        flag = True
        for j in range(c+1, len(board)):
            if board[r][j] == 1:
                flag = False
                break
        if flag:
            for j in range(c+1, len(board)):
                board[r][j] = 1
                cnt += 1
        else:
            return -1
    elif direction == 2:
        flag = True
        for i in range(r + 1, len(board)):
            if board[i][c] == 1:
                flag = False
                break
        if flag:
            for i in range(r + 1, len(board)):
                board[i][c] = 1
                cnt += 1
        else:
            return -1
    elif direction == 3:
        flag = True
        for j in range(c):
            if board[r][j] == 1:
                flag = False
                break
        if flag:
            for j in range(c):
                board[r][j] = 1
                cnt += 1
        else:
            return -1
    return cnt

def isWrap(r, c, board):
    flags = [True, True, True, True]
    for i in range(r):
        if board[i][c] == 1:
            flags[0] = False
            break
    for j in range(c):
        if board[r][j] == 1:
            flags[1] = False
            break
    for i in range(r+1, len(board)):
        if board[i][c] == 1:
            flags[2] = False
            break
    for j in range(c+1, len(board)):
        if board[r][j] == 1:
            flags[3] = False
            break
    if flags.count(False) == 4:
        return True
    else:
        return False

N = int(input())
for i in range(N):
    cN = int(input())
    board = []
    for j in range(cN):
        board.append(list(map(int,input().split(' '))))
    print('#'+str(i+1),solution(board))

