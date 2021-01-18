import sys
rl = sys.stdin.readline
from collections import deque
nrcs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

T = int(input())
for _ in range(T):
    w, h = map(int, rl().rstrip().split())
    _map = []
    for __ in range(h):
        _map.append(list(rl().rstrip()))
    dp = [[float('inf')] * w for __ in range(h)]
    flames = []
    answer = 'IMPOSSIBLE'
    start = (0, 0)
    for r in range(h):
        for c in range(w):
            if _map[r][c] == '*':
               flames.append((r, c))
            elif _map[r][c] == '@':
                start = (r, c)
                _map[r][c] = '.'
    dp[start[0]][start[1]] = 1
    q = deque()
    q.append((start, 0))
    beforecnt = -1
    while q:
        cur = q.popleft()
        cpos = cur[0]
        cr = cpos[0]
        cc = cpos[1]
        ccnt = cur[1]

        if cr == 0 or cr == h-1 or cc == 0 or cc == w-1:
            answer = dp[cr][cc]
            break
        if beforecnt != ccnt:
            flamesLen = len(flames)
            flames2 = []
            for i in range(flamesLen):
                flame = flames.pop()
                for j in range(4):
                    nr = flame[0] + nrcs[j][0]
                    nc = flame[1] + nrcs[j][1]
                    if 0<=nr<h and 0<=nc<w:
                        if _map[nr][nc] == '.':
                            _map[nr][nc] = '*'
                            flames2.append((nr, nc))
            flames = flames2[:]
            beforecnt = ccnt

        for i in range(4):
            nr = cr + nrcs[i][0]
            nc = cc + nrcs[i][1]
            if 0 <= nr < h and 0 <= nc < w:
                if _map[nr][nc] == '.':
                    if dp[cr][cc] + 1 < dp[nr][nc]:
                        dp[nr][nc] = dp[cr][cc] + 1
                        q.append(((nr, nc), ccnt + 1))
    print(answer)