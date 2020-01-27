# 듣보잡
# https://www.acmicpc.net/problem/1764
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline
n, m = map(int, input().split(' '))

myhash = {}
listen = []
see = []
cnt = 0
answer = []
for xxx in range(n):
    myhash[rl().rstrip()] = True
for yyy in range(m):
    inp = rl().rstrip()
    if inp in myhash:
        cnt += 1
        answer.append(inp)

answer.sort()
print(cnt)
for a in answer:
    print(a)