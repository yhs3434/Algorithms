# 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775

def solution(k, n):
    answer = 0

    board = [[0 for j in range(16)] for i in range(15)]
    for i in range(1, 16):
        board[0][i] = i
    for i in range(1, 15):
        for j in range(1, 15):
            board[i][j] = board[i][j-1] + board[i-1][j]

    answer = board[k][n]

    return answer

t = int(input())

for xxx in range(t):
    k = int(input())
    n = int(input())
    print(solution(k, n))