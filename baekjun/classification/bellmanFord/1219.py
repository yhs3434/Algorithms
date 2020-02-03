# 오민식의 고민
# https://www.acmicpc.net/problem/1219
# https://github.com/yhs3434/Algorithms

from collections import deque

n, s, e, m = map(int, input().split(' '))
adj = {}
for i in range(n):
    adj[i] = {}
for _ in range(m):
    u, v, w = map(int, input().split(' '))
    if v not in adj[u]:
        adj[u][v] = -w
    else:
        adj[u][v] = max(-w, adj[u][v])
dest = list(map(int, input().split(' ')))
dp = [-float('inf')] * n
dp[s] = dest[s]

cycles = set()

cnt = 0
update = True
while update and cnt != n:
    update = False
    for here in range(n):
        for there in adj[here]:
            nextMoney = dp[here] + adj[here][there] + dest[there]
            if dp[here] != -float('inf') and nextMoney > dp[there]:
                if cnt == n-1:
                    cycles.add(here)
                dp[there] = nextMoney
                update = True
    cnt += 1

geeFlag = False
q = deque()
cycles= list(cycles)
if e in cycles:
    geeFlag = True
visit = [False] * n
for cycle in cycles:
    q.append(cycle)
while q:
    cur = q.popleft()
    here = cur

    if visit[here]:
        continue
    visit[here] = True

    for there in adj[here]:
        if there == e:
            geeFlag = True
            break
        else:
            q.append(there)
    if geeFlag == True:
        break

if dp[e] == -float('inf'):
    print('gg')
elif geeFlag:
    print('Gee')
else:
    print(dp[e])