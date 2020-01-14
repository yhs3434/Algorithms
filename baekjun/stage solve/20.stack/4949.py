# 균형잡힌 세상
# https://www.acmicpc.net/problem/4949

import sys
rl = sys.stdin.readline

def solution(strr):
    st = []
    for c in strr:
        if c == '[':
            st.append(c)
        elif c == '(':
            st.append(c)
        elif c == ']':
            if st:
                if st[-1] == '[':
                    st.pop()
                else:
                    return 'no'
            else:
                return 'no'
        elif c == ')':
            if st:
                if st[-1] == '(':
                    st.pop()
                else:
                    return 'no'
            else:
                return 'no'
    if st:
        return 'no'
    else:
        return 'yes'

while True:
    strr = rl().rstrip()
    if strr == '.':
        break
    print(solution(strr))