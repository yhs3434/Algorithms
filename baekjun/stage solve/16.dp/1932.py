# 정수 삼각형
# https://www.acmicpc.net/problem/1932

def solution(n, board):
    for i in range(1, n):
        board[i][0] += board[i-1][0]
        for j in range(1, i):
            board[i][j] += max(board[i-1][j-1], board[i-1][j])
        board[i][-1] += board[i-1][-1]
    return max(board[-1])

n = int(input())
board = []
for xxx in range(n):
    board.append(list(map(int, input().split(' '))))
print(solution(n, board))