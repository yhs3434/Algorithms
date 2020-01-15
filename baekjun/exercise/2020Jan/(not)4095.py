# 최대 정사각형
# https://www.acmicpc.net/problem/4095

import sys
rl = sys.stdin.readline

def solution(n, m, board):
    cLen = min(n, m)
    while cLen > 0:
        flag = False
        for i in range(n-cLen+1):
            for j in range(m - cLen+1):
                if isRight(i, j, cLen, board):
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
        cLen -= 1
    return cLen

def isRight(r, c, cLen, board):
    for i in range(cLen):
        for j in range(cLen):
            if board[r+i][c+j] == 0:
                return False
    return True

while True:
    n, m = map(int, rl().rstrip().split(' '))
    if n==0 and m==0:
        break
    board = []
    for xxx in range(n):
        board.append(list(map(int, rl().rstrip().split(' '))))
    print(solution(n, m, board))