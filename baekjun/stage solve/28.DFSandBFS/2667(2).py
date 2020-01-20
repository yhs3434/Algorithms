# 단지번호붙이기
# https://www.acmicpc.net/problem/2667
# https://github.com/yhs3434

import sys
rl = sys.stdin.readline
from collections import deque

n = int(rl().rstrip())
board = []
for i in range(n):
    board.append(rl().rstrip())
dp = [[0]*n for i in range(n)]

q = deque()
cnt = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0 and board[i][j] =='1':
            cnt += 1
            q.append((i, j, cnt)) # (r, c, cnt)
            dp[i][j] = cnt
            while q:
                cur = q.popleft()
                r = cur[0]
                c = cur[1]
                cCnt = cur[2]

                if r-1 >= 0 and board[r-1][c] == '1' and dp[r-1][c] == 0:
                    dp[r-1][c] = cCnt
                    q.append((r-1, c, cCnt))
                if c+1 < n and board[r][c+1] == '1' and dp[r][c+1] == 0:
                    dp[r][c+1] = cCnt
                    q.append((r, c+1, cCnt))
                if r+1 < n and board[r+1][c] == '1' and dp[r+1][c] == 0:
                    dp[r + 1][c] = cCnt
                    q.append((r+1, c, cCnt))
                if c-1 >= 0 and board[r][c-1] == '1' and dp[r][c-1] == 0:
                    dp[r][c-1] = cCnt
                    q.append((r, c-1, cCnt))
cnt = 0
cnthash = {}
for i in range(n):
    for j in range(n):
        if dp[i][j] > 0:
            if dp[i][j] not in cnthash:
                cnthash[dp[i][j]] = 1
                cnt += 1
            else:
                cnthash[dp[i][j]] += 1
cnts = []
for key in cnthash:
    cnts.append(cnthash[key])
if cnts:
    cnts.sort()
    print(cnt)
    for c in cnts:
        print(c)
else:
    print(0)