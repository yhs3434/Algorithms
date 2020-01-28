# 양
# https://www.acmicpc.net/problem/3184
# https://github.com/yhs3434/Algorithms

from collections import deque

nrcs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

n, m = map(int, input().split(' '))
board = []
for _ in range(n):
    board.append(list(input()))
visited = [[False] * (m) for _ in range(n)]

cnts = [0, 0]
q = deque()

for i in range(n):
    for j in range(m):
        if not visited[i][j] and (board[i][j] == 'v' or board[i][j] == 'o'):
            visited[i][j] = True
            cCnts = [0, 0]
            if board[i][j] == 'v':
                cCnts[1] += 1
            else:
                cCnts[0] += 1
            q.append((i, j))
            while q:
                cur = q.popleft()
                r = cur[0]
                c = cur[1]
                for _ in range(4):
                    nr = r + nrcs[_][0]
                    nc = c + nrcs[_][1]
                    if 0<=nr<n and 0<=nc<m:
                        if not visited[nr][nc] and board[nr][nc] != '#':
                            visited[nr][nc] = True
                            if board[nr][nc] == 'v':
                                cCnts[1] += 1
                            elif board[nr][nc] == 'o':
                                cCnts[0] += 1
                            q.append((nr, nc))
            if cCnts[0] > cCnts[1]:
                cnts[0] += cCnts[0]
            else:
                cnts[1] += cCnts[1]
for cnt in cnts:
    print(cnt, end=' ')