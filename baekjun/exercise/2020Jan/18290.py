# NM과 K (1)
# https://www.acmicpc.net/problem/18290
# https://github.com/yhs3434/Algorithms

from collections import deque

nrcs = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]

N, M, K = map(int, input().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, input().split(' '))))

answer = -float('inf')
q = deque()

for r in range(N):
    for c in range(M):
        q.append(([(r, c)], 1))

while q:
    cur = q.popleft()
    pos = cur[0]
    r = cur[0][-1][0]
    c = cur[0][-1][1]
    cCnt = cur[1]

    if cCnt == K:
        val = 0
        for p in pos:
            val += board[p[0]][p[1]]
        if val > answer:
            answer = val
    else:
        for i in range(r, N):
            for j in range(M):
                if (i,j) in pos or (i, j-1) in pos or (i, j+1) in pos or (i-1,j) in pos or (i+1, j) in pos:
                    continue
                else:
                    q.append((cur[0] + [(i, j)], cCnt+1))
print(answer)