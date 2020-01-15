# 쿼드트리
# https://www.acmicpc.net/problem/1992

def solution(n, board):
    printRight(n, 0, 0, board)
    return

def printRight(n, r, c, board):
    if isRight(n, r, c, board):
        print(board[r][c], end='')
    else:
        n = n//2
        print('(', end='')
        printRight(n, r, c, board)
        printRight(n, r, c+n, board)
        printRight(n, r+n, c, board)
        printRight(n, r+n, c+n, board)
        print(')', end='')

def isRight(n, r, c, board):
    color = board[r][c]
    for i in range(n):
        for j in range(n):
            if board[r+i][c+j] != color:
                return False
    return True

n = int(input())
board = []
for xxx in range(n):
    board.append(input())
solution(n, board)