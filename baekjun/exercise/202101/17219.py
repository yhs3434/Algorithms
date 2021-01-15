N, M = map(int, input().split())
pws = {}
for _ in range(N):
    key, val = input().split()
    pws[key] = val
for _ in range(M):
    key = input()
    print(pws[key])