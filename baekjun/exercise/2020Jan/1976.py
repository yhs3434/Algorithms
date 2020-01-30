# 여행 가자
# https://www.acmicpc.net/problem/1976
# https://github.com/yhs3434/Algorithms

from heapq import heappush, heappop

def isGo(N, adj, u, v):
    pq = []
    dist = [float('inf')] * N
    dist[u] = 0
    heappush(pq, (0, u))
    while pq:
        cur = heappop(pq)
        cost = cur[0]
        here = cur[1]

        for there in range(N):
            if adj[here][there] == 1:
                nextDist = cost + 1
                if nextDist < dist[there]:
                    dist[there] = nextDist
                    heappush(pq, (nextDist, there))
    if dist[v] == float('inf'):
        return False
    else:
        return True

N = int(input())
M = int(input())
adj = []
for _ in range(N):
    adj.append(list(map(int, input().split(' '))))
arr = list(map(int, input().split(' ')))

flag = True
for i in range(1, len(arr)):
    if not isGo(N, adj, arr[i-1]-1, arr[i]-1):
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")