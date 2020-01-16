# 별 찍기 - 6
# https://www.acmicpc.net/problem/2443

n = int(input())

for i in range(n, 0, -1):
    for j in range(n-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*', end='')
    print('')
