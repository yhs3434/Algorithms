# 욕심쟁이 판다
# https://www.acmicpc.net/problem/1937
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline
from collections import deque
import sys
sys.setrecursionlimit(10**6)

nrcs = [[-1, 0],  [1, 0], [0, -1], [0, 1]]

ans = 0

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,rl().rstrip().split(' '))))
dp = [[-1]*n for _ in range(n)]

def dfs(r, c):
    if dp[r][c] > 0:
        return dp[r][c]
    dp[r][c] = 1

    for _ in range(4):
        nr = nrcs[_][0] + r
        nc = nrcs[_][1] + c
        if 0<=nr<n and 0<=nc<n:
            if board[nr][nc] > board[r][c]:
                dp[r][c] = max(dp[r][c], dfs(nr, nc)+1)
    return dp[r][c]

ans = 0
for r in range(n):
    for c in range(n):
        ans = max(ans, dfs(r, c))
print(ans)