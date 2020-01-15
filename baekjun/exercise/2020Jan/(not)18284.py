# Idilični Instagram
# https://www.acmicpc.net/problem/18284

def solution(board):
    i = 0
    while i<len(board):
        row = board[i]
    return

n = int(input())
board = []
cnt = 0
while True:
    row = input()
    temp = [None,None,None]
    cnt += len(row)
    if len(row) >= 1:
        temp[0] = row[0]
    if len(row) >=2:
        temp[1] = row[1]
    if len(row) >= 3:
        temp[2] = row[2]
    board.append(temp)
    if cnt >= n:
        break

solution(board)