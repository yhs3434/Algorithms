# 별 찍기 - 17
# https://www.acmicpc.net/problem/10992

n = int(input())

for i in range(1, n+1):
    if i==n:
        for j in range(2*i-1):
            print('*', end='')
    elif i==1:
        for j in range(n-i):
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