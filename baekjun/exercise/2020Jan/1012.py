# 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys
rl = sys.stdin.readline

def solution(cabs):
    cnt = 0
    while cabs:
        cnt += 1
        st = []
        st.append(cabs.pop())
        while st:
            cur = st.pop()
            r = cur[0]
            c = cur[1]
            if (r-1, c) in cabs:
                cabs.remove((r-1, c))
                st.append((r-1, c))
            if (r, c+1) in cabs:
                cabs.remove((r, c+1))
                st.append((r, c+1))
            if (r+1, c) in cabs:
                cabs.remove((r+1, c))
                st.append((r+1, c))
            if (r, c-1) in cabs:
                cabs.remove((r, c-1))
                st.append((r, c-1))

    return cnt

t = int(input())
for xxx in range(t):
    cabs = []
    m, n, k = map(int, rl().rstrip().split(' '))
    for yyy in range(k):
        cabs.append(tuple(map(int, rl().rstrip().split(' '))))
    print(solution(cabs))