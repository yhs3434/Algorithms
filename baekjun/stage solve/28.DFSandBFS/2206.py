# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206
# https://github.com/yhs3434

from collections import deque

nrcs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

n, m = map(int, input().split(' '))
board = []
for xxx in range(n):
    inp = input()
    board.append(inp)

dp1 = [[float('inf')] * m for i in range(n)]
dp1[0][0] = 1
dp0 = [[float('inf')] * m for i in range(n)]

q = deque()
q.append((0, 0, 1))  # (r, c, destroy)

while q:
    cur = q.popleft()
    r = cur[0]
    c = cur[1]
    destroyCnt = cur[2]

    if r == n-1 and c == m-1:
        continue

    if destroyCnt > 0:
        for nrc in nrcs:
            nr = nrc[0] + r
            nc = nrc[1] + c
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == '0':
                    if dp1[r][c] + 1 < dp1[nr][nc]:
                        q.append((nr, nc, destroyCnt))
                        dp1[nr][nc] = dp1[r][c] + 1
                else:
                    if dp1[r][c] + 1 < dp0[nr][nc]:
                        q.append((nr, nc, destroyCnt-1))
                        dp0[nr][nc] = dp1[r][c] + 1
    else:
        for nrc in nrcs:
            nr = nrc[0] + r
            nc = nrc[1] + c
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == '0':
                    if dp0[r][c] + 1 < dp0[nr][nc]:
                        q.append((nr, nc, destroyCnt))
                        dp0[nr][nc] = dp0[r][c] + 1


if dp1[-1][-1] == float('inf') and dp0[-1][-1] == float('inf'):
    print(-1)
else:
    print(min(dp1[-1][-1], dp0[-1][-1]))