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
        st.append(i)

    while st:
        cur = st.pop()
