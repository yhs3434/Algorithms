# 별 찍기 - 5
# https://www.acmicpc.net/problem/2442

n = int(input())

for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*', end='')
    print('')