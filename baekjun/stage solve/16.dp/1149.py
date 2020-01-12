# RGB 거리
# https://www.acmicpc.net/problem/1149

def solution(board):
    n = len(board)
    for i in range(1, n):
        board[i][0] += min(board[i-1][1], board[i-1][2])
        board[i][1] += min(board[i - 1][0], board[i - 1][2])
        board[i][2] += min(board[i - 1][0], board[i - 1][1])
    return min(board[-1])

N = int(input())
board = []
for xxx in range(N):
    board.append(list(map(int, input().split(' '))))
print(solution(board))