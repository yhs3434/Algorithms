# 축사 배정
# https://www.acmicpc.net/problem/2188

N, M = map(int, input().split())

adj = {}
for i in range(1, N+1):
    k, *arr = map(int, input().split())
    adj[i] = arr

amatch = [0] * (N+1)
bmatch = [0] * (M+1)
visited = [False] * (N+1)

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
answer = 0
for start in range(1, N+1):
    visited = [False] * (N+1)
    if dfs(start):
        answer += 1
print(answer)