# 색종이 만들기
# https://www.acmicpc.net/problem/2630

def solution(n, board):
    cHash = {0: 0, 1: 0}
    getCnt(n, 0, 0, board, cHash)
    print(cHash[0])
    print(cHash[1])
    return

def getCnt(n, r, c, board, cHash):
    if isRight(n, r, c, board):
        cHash[board[r][c]] += 1
    else:
        n = n//2
        getCnt(n, r, c, board, cHash)
        getCnt(n, r+n, c, board, cHash)
        getCnt(n, r, c+n, board, cHash)
        getCnt(n, r+n, c+n, board, cHash)

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