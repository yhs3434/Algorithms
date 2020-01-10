# 수 정렬하기 2
# https://www.acmicpc.net/problem/2751

import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for xxx in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
for a in arr:
    print(a)