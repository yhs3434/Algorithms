import sys
sys.stdin = open('1/in5.txt', 'r')
from collections import deque

N, M = map(int, input().rstrip().split())
arr = []
for i in range(N):
    score, spend = map(int, input().rstrip().split())
    arr.append((score, spend))

q = deque()
q.append((0, 0, arr))   # (score, time, problems.arr)
answer = 0
while q:
    cur = q.popleft()
    cscore = cur[0]
    ctime = cur[1]
    cproblems = cur[2]

    cproblem = cproblems[0]
    crest = cproblems[1:]
    score, spend = cproblem

    if len(crest) > 0:
        if ctime + spend <= M:
            q.append((cscore + score, ctime + spend, crest))
        q.append((cscore, ctime, crest))
    else:
        if ctime + spend <= M:
            answer = max(answer, cscore + score)
        else:
            answer = max(answer, cscore)

print(answer)