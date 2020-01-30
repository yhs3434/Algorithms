# N과 M (6)
# https://www.acmicpc.net/problem/15655
# https://github.com/yhs3434/Algorithms

from collections import deque
from itertools import combinations

n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.sort()

answer = list(combinations(arr, m))
for row in answer:
    for a in row:
        print(a, end=' ')
    print('')