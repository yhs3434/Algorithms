# 노트북의 주인을 찾아서
# https://www.acmicpc.net/problem/1298
# https://github.com/yhs3434/algorithms
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
adj = {}
for i in range(1, 1001):
    adj[i] = []
for _ in range(m):
    a, b = map(int,input().split())
    adj[a].append(b)

amatch = [0] * (1001)
bmatch = [0] * (1001)
visited = [False] * (1001)

def dfs(here):
    if visited[here]:
        return False
    visited[here] = True

    for there in adj[here]:
        if bmatch[there]==0 or dfs(bmatch[there]):
            amatch[here] = there
            bmatch[there] = here
            return True
    return False

ans = 0
for start in range(1, n+1):
    visited = [False] * (1001)
    if dfs(start):
        ans += 1
print(ans)