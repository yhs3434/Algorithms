# 종이의 개수
# https://www.acmicpc.net/problem/1780

def solution(n, board):
    lHash = {-1: 0, 0: 0, 1: 0}
    printRight(n, 0, 0, board, lHash)
    print(lHash[-1])
    print(lHash[0])
    print(lHash[1])
    return

def printRight(n, r, c, board, lHash):
    if isRight(n, r, c, board):
        lHash[board[r][c]] += 1
    else:
        n = n//3
        printRight(n, r, c, board, lHash)
        printRight(n, r, c + n, board, lHash)
        printRight(n, r, c + 2*n, board, lHash)
        printRight(n, r + n, c, board, lHash)
        printRight(n, r + n, c + n, board, lHash)
        printRight(n, r + n, c + 2*n, board, lHash)
        printRight(n, r + 2 * n, c, board, lHash)
        printRight(n, r + 2 * n, c + n, board, lHash)
        printRight(n, r + 2 * n, c + 2 * n, board, lHash)

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
    board.append(list(map(int, input().split(' '))))
solution(n, board)