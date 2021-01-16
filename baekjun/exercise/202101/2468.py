import sys
sys.setrecursionlimit(10**6)
nrcs = [[0, 1], [-1, 0], [0, -1], [1, 0]]

N = int(input())
arr = []
maxVal = 0
minVal = float('inf')
for _ in range(N):
    inp = list(map(int, input().split()))
    arr.append(inp)
    maxVal = max(maxVal, max(inp))
    minVal = min(minVal, min(inp))

def checkcheck(r, c, depth, N):
    for _ in range(4):
        nr = r + nrcs[_][0]
        nc = c + nrcs[_][1]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > depth and check[nr][nc] == False:
            check[nr][nc] = True
            checkcheck(nr, nc, depth, N)

maxCnt = 0
for depth in range(minVal-1, maxVal):
    cnt = 0
    check = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] > depth and not check[r][c]:
                cnt += 1
                check[r][c] = True
                checkcheck(r, c, depth, N)
    maxCnt = max(maxCnt, cnt)
print(maxCnt)