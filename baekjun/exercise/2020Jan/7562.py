# 나이트의 이동
# https://www.acmicpc.net/problem/7562
# https://github.com/yhs3434

import sys
rl = sys.stdin.readline
from collections import deque

availMove = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

t = int(input())
for xxx in range(t):
    l = int(input())
    cblock = list(map(int, rl().rstrip().split(' ')))
    nblock = list(map(int, rl().rstrip().split(' ')))

    answer = 0
    q = deque()
    q.append((cblock, 0))
    #st = []
    #st.append((cblock, 0))
    visited = [[False]*l for j in range(l)]
    visited[cblock[0]][cblock[1]] = True
    while q:
        curr = q.popleft()
        cur = curr[0]
        cnt = curr[1]

        if cur == nblock:
            answer = cnt
            break

        for i in range(8):
            nex = [cur[0] + availMove[i][0], cur[1] + availMove[i][1]]
            if nex[0] < l and nex[1] < l and nex[0] >= 0 and nex[1] >= 0 and not visited[nex[0]][nex[1]]:
                q.append((nex, cnt + 1))
                visited[nex[0]][nex[1]] = True
    print(answer)