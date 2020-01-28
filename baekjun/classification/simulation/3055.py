# 탈출
# https://www.acmicpc.net/problem/3055
# https://github.com/yhs3434/Algorithms

from collections import deque

nrcs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

n, m = map(int, input().split(' '))
board = []
for xxx in range(n):
    board.append(list(input()))
dp = [[float('inf')] * m for _ in range(n)]

sr, sc = 0, 0
dr, dc = 0, 0
waters = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            sr, sc = i, j
        elif board[i][j] == '*':
            waters.append((i, j))
        elif board[i][j] == 'D':
            dr, dc = i, j

dp[sr][sc] = 0

q = deque()
for water in waters:
    q.append((water[0], water[1], '*'))
q.append((sr, sc, 'g'))

while q:
    cur = q.popleft()
    r = cur[0]
    c = cur[1]
    gw = cur[2]

    if gw == '*':
        for _ in range(4):
            nr = r + nrcs[_][0]
            nc = c + nrcs[_][1]
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == '.':
                    board[nr][nc] = '*'
                    q.append((nr, nc, '*'))
    elif gw == 'g':
        for _ in range(4):
            nr = r + nrcs[_][0]
            nc = c + nrcs[_][1]
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == '.':
                    if dp[r][c] + 1 < dp[nr][nc]:
                        dp[nr][nc] = dp[r][c] + 1
                        q.append((nr, nc, 'g'))
                elif board[nr][nc] == 'D':
                    if dp[r][c] + 1 < dp[nr][nc]:
                        dp[nr][nc] = dp[r][c] + 1
if dp[dr][dc] != float('inf'):
    print(dp[dr][dc])
else:
    print('KAKTUS')