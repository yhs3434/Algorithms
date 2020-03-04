# 돌맹이 제거
# https://www.acmicpc.net/problem/1867
# https://github.com/yhs3434/algorithms

n, k = map(int, input().split())
adj = {}
for i in range(1, n+1):
    adj[i] = []
for i in range(k):
    a, b = map(int, input().split())
    adj[a].append(b)

amatch = [0] * (n+1)
bmatch = [0] * (n+1)
visited = [0 for _ in range(n+1)]
visitCnt = 0

def dfs(here):
    if visited[here] >= visitCnt:
        return False
    visited[here] += 1

    for there in adj[here]:
        if bmatch[there] == 0 or dfs(bmatch[there]):
            amatch[here] = there
            bmatch[there] = here
            return True
    return False
ans = 0
for start in range(1, n+1):
    visitCnt += 1
    if dfs(start):
        ans += 1
print(ans)