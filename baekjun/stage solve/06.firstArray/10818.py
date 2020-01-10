# 최소 최대
# https://www.acmicpc.net/problem/10818

import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
print(min(arr),max(arr))