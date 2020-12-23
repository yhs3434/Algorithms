from collections import deque
import sys
sys.stdin = open('4input/in5.txt', 'r')

nrcs = [[0, 1], [1, 0]]

n = int(input())
arr = []
for i in range(n):
    temp = list(map(int, input().rstrip().split(' ')))
    arr.append(temp)
dp = [[float('inf') for _ in range(n)] for __ in range(n)]

dp[0][0] = arr[0][0]
q = deque()
q.append((0, 0, arr[0][0]))
while q:
    cur = q.popleft()
    cr = cur[0]
    cc = cur[1]
    cval = cur[2]

    for _ in range(2):
        nr = cr + nrcs[_][0]
        nc = cc + nrcs[_][1]
        if nr < n and nc < n:
            if dp[cr][cc] + arr[nr][nc] <= dp[nr][nc]:
                dp[nr][nc] = dp[cr][cc] + arr[nr][nc]
                q.append((nr, nc, dp[cr][cc] + arr[nr][nc]))

print(dp[-1][-1])