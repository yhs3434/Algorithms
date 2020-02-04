# 모든 순열
# https://www.acmicpc.net/problem/10974
# https://github.com/yhs3434/Algorithms

from itertools import permutations

n = int(input())

answer = list(permutations([i for i in range(1, n+1)], n))
for a in answer:
    for x in a:
        print(x, end=' ')
    print('')