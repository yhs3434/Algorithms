# 괄호
# https://www.acmicpc.net/problem/9012

def solution(pt):
    st = 0
    for p in pt:
        if p=='(':
            st += 1
        elif p==')':
            st -= 1
        if st<0:
            break
    if st==0:
        return 'YES'
    else:
        return 'NO'

n = int(input())
for xxx in range(n):
    print(solution(input()))