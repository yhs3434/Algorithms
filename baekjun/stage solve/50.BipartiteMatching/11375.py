# 열혈강호
# https://www.acmicpc.net/problem/11375
# https://github.com/yhs3434/Algorithms

import sys
#sys.setrecursionlimit(10*6)
input = sys.stdin.readline
#print = sys.stdout.write

N, M = map(int, input().split())
adj = {}
visited = {}
amatch = {}
bmatch = {}

for i in range(1, 1001):
    adj[i] = []
    visited[i] = 0
    amatch[i] = 0
    bmatch[i] = 0

for i in range(1, N+1):
    s = input().split()
    for j in range(1, len(s)):
        adj[i].append(int(s[j]))

answer = 0

def dfs(a):
    visited[a] = 1

    for b in adj[a]:
        if bmatch[b] == 0 or visited[bmatch[b]] == 0 and dfs(bmatch[b]):
            amatch[a] = b
            bmatch[b] = a

            return 1

    return 0

def dictReset(mydict):
    for i in range(1, len(mydict) + 1): mydict[i] = 0

for start in range(1, N+1):
    if amatch[start] == 0:
        dictReset(visited)
        if dfs(start):
            answer += 1

print(str(answer))