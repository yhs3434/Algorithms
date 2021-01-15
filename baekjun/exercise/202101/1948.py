import sys
rl = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
m = int(input())

adj = {}
visited = [False] * (n+1)
edge_visited = {}
dp = [0] * (n+1)
cnt = 0
cost_cache = 0

for _ in range(m):
    a, b, t = map(int, rl().rstrip().split())
    if a not in adj:
        adj[a] = {b: t}
        edge_visited[a] = {b: False}
    else:
        adj[a][b] = t
        edge_visited[a][b] = False

s, e = map(int, rl().rstrip().split())

def dfs(here):
    if here == e:
        return 0
    for there in adj[here]:
        if not visited[there]:
            dp[here] = max(dp[here], dfs(there) + adj[here][there])
        else:
            dp[here] = max(dp[here], dp[there] + adj[here][there])
    visited[here] = True
    return dp[here]
max_cost = dfs(s)
cnt = 0

def dfs2(here, cost, maxCost):
    ret = 0
    if cost + dp[here] == maxCost:
        ret += 1
    else:
        return 0
    if here in adj:
        for there in adj[here]:
            if not edge_visited[here][there]:
                ret += dfs2(there, cost + adj[here][there], maxCost)
                edge_visited[here][there] = True
    return ret

print(max_cost)
cnt = dfs2(s, 0, max_cost)
print(cnt-1)