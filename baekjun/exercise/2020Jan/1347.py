# 미로 만들기
# https://www.acmicpc.net/problem/1347
# https://github.com/yhs3434/Algorithms

n = int(input())
inp = input()

def getNext(f):
    if f == 0:
        return [-1, 0]
    elif f == 1:
        return [0, 1]
    elif f == 2:
        return [1, 0]
    elif f == 3:
        return [0, -1]

cur = (0, 0)
d = 2
visited = [cur]
for ch in inp:
    r = cur[0]
    c = cur[1]

    if ch == 'R':
        d = (d + 1) % 4
    elif ch == 'L':
        d = (d + 3) % 4
    elif ch == 'F':
        nex = getNext(d)
        nr = r + nex[0]
        nc = c + nex[1]
        cur = (nr, nc)
        visited.append(cur)
minR = float('inf')
minC = float('inf')
maxR = -float('inf')
maxC = -float('inf')
for visit in visited:
    if visit[0] < minR:
        minR = visit[0]
    if visit[1] < minC:
        minC = visit[1]
    if visit[0] > maxR:
        maxR = visit[0]
    if visit[1] > maxC:
        maxC = visit[1]

N = (maxR - minR) + 1
M = (maxC - minC) + 1
board = [['#']*M for _ in range(N)]
for visit in visited:
    r = visit[0] - minR
    c = visit[1] - minC

    board[r][c] = '.'

for row in board:
    for col in row:
        print(col, end='')
    print('')