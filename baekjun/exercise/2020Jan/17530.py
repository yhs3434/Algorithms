# Buffoon
# https://www.acmicpc.net/problem/17530
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(rl().rstrip()))

if arr[0] == max(arr):
    print('S')
else:
    print('N')