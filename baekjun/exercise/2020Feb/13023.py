# ABCDE
# https://www.acmicpc.net/problem/13023
# https://github.com/yhs3434/Algorithms


N, M = map(int, input().split(' '))
adj = {}
for i in range(N):
    adj[i] = {}

for _ in range(M):
    u, v = map(int, input().split(' '))
    adj[u][v] = 1
    adj[v][u] = 1

visited = [False] * N
flag = True
for start in range(N):
    if not flag:
        break
    cVisited = visited[:]
    cVisited[start] = True
    st = []
    st.append((start, 0, [start]))
    while st and flag:
        cur = st.pop()
        here = cur[0]
        cCnt = cur[1]
        path = cur[2]

        for there in adj[here]:
            if there not in path:
                if cCnt + 1 >= 4:
                    flag = False
                    break
                st.append((there, cCnt+1, path+[there]))


if not flag:
    print(1)
else:
    print(0)