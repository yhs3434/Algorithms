# 걷다보니 신천역 삼 (small)
# https://www.acmicpc.net/problem/14650
# https://github.com/yhs3434/Algorithms

from collections import deque

n = int(input())

cnt = 0
q = deque()
visited = {}
for i in range(1, 3):
    q.append(([i], i, 1))    # (sumVal, len)

while q:
    cur = q.popleft()
    arr = cur[0]
    sumVal = cur[1]
    cLen = cur[2]

    if cLen==n and sumVal % 3 == 0:
        cnt += 1

    for i in range(3):
        nArr = arr + [i]
        if str(nArr) not in visited and cLen+1 <= n:
            visited[str(nArr)] = True
            q.append((nArr, sumVal+i, cLen+1))
print(cnt)