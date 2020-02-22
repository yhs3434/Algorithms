# 내리막 길
# https://www.acmicpc.net/problem/1520
# https://github.com/yhs3434/Algorithms

from collections import deque
import sys
sys.setrecursionlimit(10**6)

nrcs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N, M = map(int, input().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, input().split(' '))))

dp = [[-1]*M for _ in range(N)]
dp[-1][-1] = 1

def goDp(r, c):
    if r==N-1 and c==M-1:
        return dp[-1][-1]
    if dp[r][c] == -1:
        dp[r][c] = 0
        for i in range(4):
            nr = r + nrcs[i][0]
            nc = c + nrcs[i][1]
            if 0<=nr<N and 0<=nc<M:
                if board[nr][nc] < board[r][c]:
                    dp[r][c] += goDp(nr, nc)
    return dp[r][c]
goDp(0, 0)
print(dp[0][0])