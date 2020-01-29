# 알고스팟
# https://www.acmicpc.net/problem/1261
# https://github.com/yhs3434/Algorithms

from collections import deque

nrcs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

m, n = map(int, input().split(' '))
board = []
for _ in range(n):
    board.append(list(map(int, list(input()))))

dp = [[float('inf')] * m for _ in range(n)]
dp[0][0] = 0

q = deque()
q.append((0, 0)) # (r, c, cnt)

while q:
    cur = q.popleft()
    r = cur[0]
    c = cur[1]

    for i in range(4):
        nr = r + nrcs[i][0]
        nc = c + nrcs[i][1]
        if 0 <= nr < n and 0 <= nc < m:
            if board[nr][nc] == 0:
                if dp[r][c] < dp[nr][nc]:
                    dp[nr][nc] = dp[r][c]
                    q.append((nr, nc))
            else:
                if dp[r][c] + 1 < dp[nr][nc]:
                    dp[nr][nc] = dp[r][c] + 1
                    q.append((nr, nc))

print(dp[-1][-1])