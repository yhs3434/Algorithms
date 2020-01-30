# 녹색 옷 입은 애가 젤다지?
# https://www.acmicpc.net/problem/4485
# https://github.com/yhs3434/Algorithms

from collections import deque

nrcs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
i = 0
while True:
    i += 1
    n = int(input())
    if n == 0:
        break

    board = []
    for _ in range(n):
        board.append(list(map(int, input().split(' '))))

    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = board[0][0]

    q = deque()
    q.append((0, 0))    # (r, c)

    while q:
        cur = q.popleft()
        r = cur[0]
        c = cur[1]

        for _ in range(4):
            nr = nrcs[_][0] + r
            nc = nrcs[_][1] + c

            if 0<=nr<n and 0<=nc<n:
                if dp[r][c] + board[nr][nc] < dp[nr][nc]:
                    dp[nr][nc] = dp[r][c] + board[nr][nc]
                    q.append((nr, nc))
    print('Problem '+str(i)+':', dp[-1][-1])