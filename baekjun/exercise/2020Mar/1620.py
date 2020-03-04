# 나는야 포켓몬 마스터
# https://www.acmicpc.net/problem/1620

import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
poketmons1 = {}
poketmons2 = {}

for _ in range(n):
    inp = input()
    poketmons1[_+1] = inp
    poketmons2[inp] = _ + 1

for _ in range(m):
    inp = input()
    try:
        inp = int(inp)
        print(poketmons1[inp])
    except:
        print(poketmons2[inp])