# 그림
# https://www.acmicpc.net/problem/1926

from collections import deque

nrcs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

n, m = map(int, input().split(' '))
board = []
for _ in range(n):
    board.append(list(map(int, input().split(' '))))

q = deque()
visited = [[False]*m for _ in range(n)]

cnt = 0
maxVal = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            cnt += 1
            visited[i][j] = True
            q.append((i, j))
            size = 1
            while q:
                cur = q.popleft()
                r = cur[0]
                c = cur[1]
                for _ in range(4):
                    nr = r + nrcs[_][0]
                    nc = c + nrcs[_][1]
                    if 0<=nr<n and 0<=nc<m:
                        if board[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            size += 1
                            q.append((nr, nc))
            if size > maxVal:
                maxVal = size
print(cnt)
print(maxVal)