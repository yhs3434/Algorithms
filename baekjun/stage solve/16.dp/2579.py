# 계단 오르기
# https://www.acmicpc.net/problem/2579

def solution(board):
    answer = 0
    bLen = len(board)
    if bLen-1 == 1:
        return board[1]
    elif bLen-1 == 2:
        return board[2] + board[1]
    dp = [[0 for j in range(2)] for i in range(bLen)]
    dp[1][0] = board[1]
    dp[1][1] = 0
    dp[2][0] = board[2]
    dp[2][1] = board[1] + board[2]
    for i in range(3, bLen):
        dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + board[i]
        dp[i][1] = dp[i-1][0] + board[i]
    answer = max(dp[-1])
    return answer

n = int(input())
board = [0]
for xxx in range(n):
    board.append(int(input()))
print(solution(board))