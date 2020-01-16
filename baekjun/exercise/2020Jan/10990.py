# 별 찍기 - 15
# https://www.acmicpc.net/problem/10990

n = int(input())

for i in range(1, n+1):
    if i == 1:
        for j in range(n - i):
            print(' ', end='')
        print('*', end='')
    else:
        for j in range(n-i):
            print(' ', end='')
        print('*', end='')
        for j in range(2*i-3):
            print(' ', end='')
        print('*', end='')
    print('')