# 왕위 계승
# https://www.acmicpc.net/problem/5021
# https://github.com/yhs3434/Algorithms

from heapq import heappop, heappush

n, m = map(int, input().split(' '))
king = input()
kingdom = {}
kingdom[king] = 1 << 20
people = []
for _ in range(n):
    s, a, b = input().split(' ')
    people.append((s, a, b))

for i in range(n):
    for j in range(n):
        s, a, b = people[j]
        kingdom[s] = 0
        if a in kingdom:
            kingdom[s] += 0.5*kingdom[a]
        if b in kingdom:
            kingdom[s] += 0.5*kingdom[b]

maxVal = 0
maxPerson = ''
for _ in range(m):
    p = input()
    if p not in kingdom:
        continue
    else:
        if kingdom[p] > maxVal:
            maxVal = kingdom[p]
            maxPerson = p
print(maxPerson)