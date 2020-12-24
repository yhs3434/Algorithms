import sys
sys.stdin = open('14.txt', 'r')
from collections import deque

answer = []
N, M = map(int, input().rstrip().split())

entries = [0] * (N+1)
adj = {}
for i in range(1, N+1):
    adj[i] = []

for i in range(M):
    a, b = map(int, input().split())
    entries[b] += 1
    adj[a].append(b)

q = deque()
while len(answer) < N:
    for i in range(1,N+1):
        if i not in answer and entries[i] == 0:
            q.append(i)
    while q:
        a = q.popleft()
        answer.append(a)
        for b in adj[a]:
            entries[b] -= 1

print(answer)