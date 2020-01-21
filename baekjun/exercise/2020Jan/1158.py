# 요세푸스 문제
# https://www.acmicpc.net/problem/1158
# https://github.com/yhs3434

from collections import deque

n, k = map(int, input().split(' '))
q = deque()
for i in range(1, n+1):
    q.append(i)
perm = []
cnt = 0
while q:
    cnt += 1
    cur = q.popleft()
    if cnt != k:
        q.append(cur)
    else:
        perm.append(cur)
        cnt = 0
answer = '<'
for i in range(len(perm)):
    p = perm[i]
    if i < len(perm)-1:
        answer += (str(p)+', ')
    else:
        answer += str(p)
answer += '>'
print(answer)