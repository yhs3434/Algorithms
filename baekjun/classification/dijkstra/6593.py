# 상범 빌딩
# https://www.acmicpc.net/problem/6593
# https://github.com/yhs3434/Algorithms

from collections import deque

nlrcs = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

while True:
    L, R, C = map(int, input().split(' '))
    if L==0 and R==0 and C==0:
        break
    board = []
    for k in range(L):
        tempBoard = []
        for i in range(R):
            tempBoard.append(list(input()))
        input()
        board.append(tempBoard)

    sl, sr, sc = 0, 0, 0
    el, er, ec = 0, 0, 0
    for k in range(L):
        for i in range(R):
            for j in range(C):
                if board[k][i][j] == 'S':
                    sl, sr, sc = k, i, j
                elif board[k][i][j] == 'E':
                    el, er, ec = k, i, j
    dp = [[[float('inf')] * C for _ in range(R)] for _ in range(L)]
    dp[sl][sr][sc] = 0

    q = deque()
    q.append((sl, sr, sc))
    while q:
        cur = q.popleft()
        l = cur[0]
        r = cur[1]
        c = cur[2]

        for _ in range(6):
            nl = nlrcs[_][0] + l
            nr = nlrcs[_][1] + r
            nc = nlrcs[_][2] + c

            if 0<=nl<L and 0<=nr<R and 0<=nc<C and board[nl][nr][nc] != '#':
                if dp[l][r][c] + 1 < dp[nl][nr][nc]:
                    dp[nl][nr][nc] = dp[l][r][c] + 1
                    q.append((nl, nr, nc))
    answer = dp[el][er][ec]
    if answer == float('inf'):
        print('Trapped!')
    else:
        print('Escaped in '+str(answer)+' minute(s).')