# 시험 점수
# https://www.acmicpc.net/problem/5596
# https://github.com/yhs3434/Algorithms

mg = list(map(int, input().split(' ')))
ms = list(map(int, input().split(' ')))

print(max(sum(mg), sum(ms)))