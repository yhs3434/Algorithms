# 택시 거리
# https://www.acmicpc.net/problem/17247
# https://github.com/yhs3434

n, m = map(int, input().split(' '))
board = []
for i in range(n):
    board.append(list(map(int, input().split(' '))))

pos = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            pos.append((i, j))
print(abs(pos[0][0] - pos[1][0]) + abs(pos[0][1] - pos[1][1]))