# 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

import sys
rl = sys.stdin.readline

n = int(rl().rstrip())
parents = [0]*(n+1)
thash = {}
for xxx in range(n-1):
    x, y = map(int, rl().rstrip().split(' '))
    if x not in thash:
        thash[x] = set([y])
    else:
        thash[x].add(y)
    if y not in thash:
        thash[y] = set([x])
    else:
        thash[y].add(x)

st = []
st.append(1)
visited = set([1])
while st:
    cur = st.pop()
    for nex in thash[cur]:
        if nex not in visited:
            st.append(nex)
            visited.add(nex)
            parents[nex] = cur
for i in range(2, len(parents)):
    print(parents[i])
