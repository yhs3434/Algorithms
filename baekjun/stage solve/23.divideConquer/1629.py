# 곱셈
# https://www.acmicpc.net/problem/1629

import sys
rl = sys.stdin.readline

def solution(a, b, c):
    ns = []
    while b > 1:
        n = a
        cnt = 1
        while cnt*2 <= b:
            n = (n*n)%c
            cnt *= 2
        b -= cnt
        ns.append(n)
    n = 1
    for x in ns:
        n = (n * x) % c
    for i in range(b):
        n = (n*a)%c
    answer = n
    return answer

a, b, c = map(int, rl().rstrip().split(' '))
print(solution(a, b, c))