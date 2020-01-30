# 칠무해
# https://www.acmicpc.net/problem/14729
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline

n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = float(rl().rstrip())
arr.sort()
for i in range(7):
    print('%.3f'%arr[i])