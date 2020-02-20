# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# https://www.acmicpc.net/problem/2422

from collections import deque
import sys
rl = sys.stdin.readline

N, M = map(int, input().split(' '))
board = [[False]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, rl().rstrip().split(' '))
    board[a][b] = True
    board[b][a] = True

q = deque()
for i in range(1, N+1):
    q.append(([i]))

answer = 0
while q:
    cArr = q.popleft()

    for i in range(cArr[-1]+1, N+1):
        if len(cArr)==1:
            if not board[cArr[0]][i]:
                q.append((cArr+[i]))
        elif len(cArr)==2:
            if not board[cArr[0]][i] and not board[cArr[1]][i]:
                answer += 1
print(answer)