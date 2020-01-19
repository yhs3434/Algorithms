# 별 찍기 - 20
# https://www.acmicpc.net/problem/10995
# https://github.com/yhs3434

n = int(input())

for i in range(n):
    if i%2 == 1:
        print(' ', end='')
    for j in range(n):
        print('*', end=' ')
    print('')