# 경기 결과

import sys
input = lambda:sys.stdin.readline().rstrip()

t = int(input())
answer = [0, 0]
for _ in range(t):
    a, b = map(int, input().split(' '))
    if a > b:
        answer[0] += 1
    elif a < b:
        answer[1] += 1
for a in answer:
    print(a, end= ' ')