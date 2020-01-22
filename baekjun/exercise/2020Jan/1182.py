# 부분수열의 합
# https://www.acmicpc.net/problem/1182
# https://github.com/yhs3434/Algorithms

from collections import deque

n, s = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

visited = [[False] * (n) for i in range(n)]

answer = 0
q = deque()
q.append((0, 0, False))
while q:
    cur = q.popleft()
    i = cur[0]
    sumVal = cur[1]
    cFlag = cur[2]
    if sumVal == s:
        if cFlag:
            answer += 1
    if i+1 <= n:
        q.append((i+1, sumVal, False))
        q.append((i + 1, sumVal+arr[i], True))

print(answer)