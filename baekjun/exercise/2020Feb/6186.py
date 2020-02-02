# Best Grass
# https://www.acmicpc.net/problem/6186
# https://github.com/yhs3434/Algorithms

from collections import deque
nrcs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

R, C = map(int, input().split(' '))
cnt = 0
board = []
for i in range(R):
    board.append(input())
visited = [[False]*C for _ in range(R)]
q = deque()
for i in range(R):
    for j in range(C):
        if not visited[i][j] and board[i][j] == '#':
            visited[i][j] = True
            q.append((i, j))
            while q:
                cur = q.popleft()
                r = cur[0]
                c = cur[1]
                for k in range(4):
                    nr = r + nrcs[k][0]
                    nc = c + nrcs[k][1]
                    if 0<=nr<R and 0<=nc<C:
                        if not visited[nr][nc] and board[nr][nc]=='#':
                            visited[nr][nc] = True
                            q.append((nr, nc))
            cnt += 1

print(cnt)