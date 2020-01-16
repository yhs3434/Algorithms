# 별 찍기 - 8
# https://www.acmicpc.net/problem/2445

n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    for j in range(n-i):
        print(' ', end='')
    for j in range(n-i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print('')
for i in range(n-1, 0, -1):
    for j in range(i):
        print('*', end='')
    for j in range(n-i):
        print(' ', end='')
    for j in range(n-i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print('')