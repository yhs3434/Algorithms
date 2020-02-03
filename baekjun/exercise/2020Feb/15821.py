# 낚이고 낚아라
# https://www.acmicpc.net/problem/15821
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline

N, K = map(int, input().split(' '))
points = []
for _ in range(N):
    p = int(rl().rstrip())
    arr = list(map(int, rl().rstrip().split(' ')))
    maxVal = 0
    for i in range(0, 2*p, 2):
        x, y = (arr[i], arr[i+1])
        val = x**2 + y**2
        if val > maxVal:
            maxVal = val
    points.append(maxVal)
points.sort()
print('%.2f'%points[K-1])