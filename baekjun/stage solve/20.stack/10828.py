# 스택
# https://www.acmicpc.net/problem/10828

import sys
rl = sys.stdin.readline

st = []

def solution(cOrd):
    if len(cOrd)>1:
        st.append(int(cOrd[1]))
    else:
        cur = cOrd[0]
        if cur == 'pop':
            if not st:
                return -1
            else:
                return st.pop()
        elif cur == 'size':
            return len(st)
        elif cur == 'empty':
            if st:
                return 0
            else:
                return 1
        elif cur == 'top':
            if not st:
                return -1
            else:
                return st[-1]

n = int(rl().rstrip())
for xxx in range(n):
    cOrder = rl().rstrip().split(' ')
    ret = solution(cOrder)
    if ret!=None:
        print(ret)