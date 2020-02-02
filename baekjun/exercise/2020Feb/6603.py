# 로또
# https://www.acmicpc.net/problem/6603
# https://github.com/yhs3434/Algorithms

from itertools import combinations

while True:
    k, *arr = map(int, input().split(' '))
    if k == 0:
        break
    answers = list(combinations(arr, 6))
    for answer in answers:
        for a in answer:
            print(a, end=' ')
        print('')
    print('')