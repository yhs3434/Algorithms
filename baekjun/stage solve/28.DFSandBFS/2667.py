# 단지번호붙이기
# https://www.acmicpc.net/problem/2667
# https://github.com/yhs3434
import numpy as np

import sys
rl = sys.stdin.readline
sys.setrecursionlimit(10**6)

def conquerDp(r, c, val, dp):
    temp = dp[r][c]
    dp[r][c] = val
    if r-1 >= 0 and dp[r-1][c] == temp:
        conquerDp(r-1, c, val, dp)
    if c-1 >= 0 and dp[r][c-1] == temp:
        conquerDp(r, c-1, val, dp)

n = int(rl().rstrip())
board = []
for i in range(n):
    board.append(rl().rstrip())

dp = [[0]*n for i in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if i == 0:
            if j == 0:
                if board[i][j] == '1':
                    cnt += 1
                    dp[i][j] = cnt
            else:
                if board[i][j] == '1':
                    if board[i][j-1] == '1':
                        dp[i][j] = cnt
                    else:
                        cnt += 1
                        dp[i][j] = cnt
        else:
            if j == 0:
                if board[i][j] == '1':
                    if dp[i-1][j] > 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        cnt += 1
                        dp[i][j] = cnt
            else:
                if board[i][j] == '1':
                    if dp[i-1][j] == 0 and dp[i][j-1] == 0:
                        cnt += 1
                        dp[i][j] = cnt
                    elif dp[i-1][j] == 0:
                        dp[i][j] = dp[i][j-1]
                    elif dp[i][j-1] == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1])
                        if dp[i-1][j] < dp[i][j-1]:
                            conquerDp(i, j-1, dp[i][j], dp)
                        else:
                            conquerDp(i-1, j, dp[i][j], dp)

cnt = 0
chash = {}
for i in range(n):
    for j in range(n):
        if dp[i][j] > 0:
            if dp[i][j] not in chash:
                chash[dp[i][j]] = 1
                cnt += 1
            else:
                chash[dp[i][j]] += 1
cnts = []
for key in chash:
    cnts.append(chash[key])
if cnts:
    cnts.sort()
    print(cnt)
    for c in cnts:
        print(c)
else:
    print(0)