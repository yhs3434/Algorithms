import sys
rl = sys.stdin.readline
from collections import deque

answer = []

N, M = map(int, input().split())
adj = {}
cnts = [0] * (N + 1)
for i in range(1, N+1):
    adj[i] = []
for _ in range(M):
    a, b = map(int, rl().rstrip().split())
    cnts[b] += 1
    adj[a].append(b)

q = deque()
while len(answer) < N:
    for i in range(1, N+1):
        if cnts[i] == 0:
            q.append(i)
            cnts[i] -= 1
    while q:
        here = q.popleft()
        answer.append(here)
        for there in adj[here]:
            cnts[there] -= 1

for ans in answer:
    print(ans, end=' ')