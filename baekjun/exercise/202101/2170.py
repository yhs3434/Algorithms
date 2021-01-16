import sys
rl = sys.stdin.readline

N = int(input())
edges = []
for _ in range(N):
    x, y = map(int, rl().rstrip().split())
    edges.append((x, y))
edges.sort()
answer = 0
s = -float('inf')
e = -float('inf')
for edge in edges:
    ns, ne = edge
    if s <= ns and ne <= e:
        continue
    answer += (ne - ns)
    if ns < e:
        answer -= (e-ns)
    s = ns
    e = ne
print(answer)
