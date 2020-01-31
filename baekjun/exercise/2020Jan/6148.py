# Bookshelf 2
# https://www.acmicpc.net/problem/6148
# https://github.com/yhs3434/Algorithms

from itertools import combinations
import sys
rl = sys.stdin.readline

N, B = map(int, input().split(' '))
arr = []
for _ in range(N):
    arr.append(int(rl().rstrip()))
avails = []
for i in range(1, N+1):
    avails.extend(list(combinations(arr, i)))
answer = float('inf')
for avail in avails:
    sumVal = sum(avail)
    if sumVal >= B:
        if sumVal-B < answer:
            answer = sumVal-B
print(answer)