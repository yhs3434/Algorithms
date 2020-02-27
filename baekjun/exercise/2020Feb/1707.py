# 이분 그래프
# https://www.acmicpc.net/problem/1707
# https://github.com/yhs3434/Algorithms

from collections import deque

K = int(input())

for _ in range(K):
    V, E = map(int, input().split(' '))
    myhash = {}
    colors = [0] * (V+1)    # 0: 미방문, 1&2: 방문
    for i in range(1, V+1):
        myhash[i] = []
    for __ in range(E):
        a, b = map(int, input().split(' '))
        myhash[a].append(b)
        myhash[b].append(a)

    st = []
    for i in range(1, V+1):
        if colors[i] == 0:
            colors[i] = 1
            st.append(i)

            while st:
                here = st.pop()
                for there in myhash[here]:
                    if colors[there] == 0:
                        colors[there] = 2 if colors[here]==1 else 1
                        st.append(there)

    flag = True
    for here in range(1, V+1):
        if flag:
            for there in myhash[here]:
                if colors[here] == colors[there]:
                    flag = False
                    break
    if flag:
        print('YES')
    else:
        print('NO')