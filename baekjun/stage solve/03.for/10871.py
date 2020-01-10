# x보다 작은 수
# https://www.acmicpc.net/problem/10871

import sys

n, x = map(int, sys.stdin.readline().split(' '))

arr = list(map(int, sys.stdin.readline().split(' ')))
answer = []
while arr:
    cur = arr.pop(0)
    if cur < x:
        answer.append(cur)
astr = ''
for a in answer:
    astr += (str(a) + ' ')
astr = astr[:-1]
print(astr)