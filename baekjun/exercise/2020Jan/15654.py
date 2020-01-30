# N과 M (5)
# https://www.acmicpc.net/problem/15654
# https://github.com/yhs3434/Algorithms

from collections import deque
from itertools import permutations

n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.sort()

answer = list(permutations(arr, m))
for row in answer:
    for a in row:
        print(a, end=' ')
    print('')