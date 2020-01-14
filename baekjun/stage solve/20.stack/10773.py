# 제로
# https://www.acmicpc.net/problem/10773

import sys
rl = sys.stdin.readline

n = int(input())
st = []
for xxx in range(n):
    num = int(rl().rstrip())
    if num == 0:
        st.pop()
    else:
        st.append(num)
print(sum(st))