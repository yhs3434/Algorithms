# 패션왕 신해빈
# https://www.acmicpc.net/problem/9375

import sys
rl = sys.stdin.readline

def solution(cs):
    n = len(cs)
    answer = 1
    for i in range(n):
        answer *= (cs[i] + 1)

    return answer-1

t = int(rl().rstrip())
for xxx in range(t):
    n = int(rl().rstrip())
    cs = {}
    for yyy in range(n):
        c = rl().rstrip().split(' ')
        if c[1] not in cs:
            cs[c[1]] = 1
        else:
            cs[c[1]] += 1
    css = []
    for key in cs:
        css.append(cs[key])
    print(solution(css))