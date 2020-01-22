# n번째 큰 수
# https://www.acmicpc.net/problem/2075
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline

def getCnt(c, board, val, n):
    cnt = 0
    for i in range(n):
        if board[i][c] < val:
            cnt += 1
        else:
            break
    return cnt

n = int(input())
board = []
left = 9999
right = 0
for xxx in range(n):
    row = list(map(int, rl().rstrip().split(' ')))
    board.append(row)
    minVal = min(row)
    maxVal = max(row)
    if minVal < left:
        left = minVal
    if maxVal > right:
        right = maxVal

n2 = n*n
answer = 0
while left <= right:
    mid = (left + right) // 2
    rank = n2
    for c in range(n):
        rank -= getCnt(c, board, mid, n)

    if rank >= n:
        left = mid + 1
        if mid > answer:
            answer = mid
    else:
        right = mid - 1

print(answer)