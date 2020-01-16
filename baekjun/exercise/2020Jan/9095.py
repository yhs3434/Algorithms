# 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095

import sys
rl = sys.stdin.readline

def solution(n):
    st = []
    st.append(n)
    cnt = 0
    while st:
        cur = st.pop()
        if cur == 0:
            cnt += 1
        elif cur > 0:
            for i in range(1, 4):
                st.append(cur - i)
    return cnt

t = int(input())
for xxx in range(t):
    n = int(rl().rstrip())
    print(solution(n))