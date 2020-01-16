# 별 찍기 - 16
# https://www.acmicpc.net/problem/10991

n = int(input())

for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end='')
    for j in range(i):
        print('*', end=' ')
    print('')