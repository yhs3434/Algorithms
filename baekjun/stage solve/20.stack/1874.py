# 스택 수열
# https://www.acmicpc.net/problem/1874

import sys
rl = sys.stdin.readline

def solution(n, prog):
    answer = []
    st = []
    cntp = 0
    cntm = 0
    j = 0
    for i in range(1, n+1):
        while st and j < n and prog[j] == st[-1]:
            st.pop()
            answer.append('-')
            cntm += 1
            j += 1
        st.append(i)
        answer.append('+')
        cntp += 1
    while st and j < n and prog[j] == st[-1]:
        st.pop()
        answer.append('-')
        cntm += 1
        j += 1
    if cntm == cntp:
        return answer
    else:
        return []

n = int(input())
prog = []
for xxx in range(n):
    prog.append(int(rl().rstrip()))
answer = solution(n, prog)
if answer:
    for a in answer:
        print(a)
else:
    print('NO')