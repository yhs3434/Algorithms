# 수 정렬하기 3
# https://www.acmicpc.net/problem/10989

import sys
line = sys.stdin.readline
arr = [0] * 10001
for i in range(int(line())):
    num = int(line())
    arr[num] += 1
for i in range(1, 10001):
    for j in range(arr[i]):
        print(i)