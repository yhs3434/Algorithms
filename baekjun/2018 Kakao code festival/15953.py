# 상금 헌터
# https://www.acmicpc.net/problem/15953

def get2017(n):
    if n == 0:
        return 0
    if n <= 1:
        return 5000000
    elif n <= 3:
        return 3000000
    elif n <= 6:
        return 2000000
    elif n <= 10:
        return 500000
    elif n <= 15:
        return 300000
    elif n <= 21:
        return 100000
    else:
        return 0

def get2018(n):
    if n == 0:
        return 0
    if n<=1:
        return 5120000
    elif n<=3:
        return 2560000
    elif n<=7:
        return 1280000
    elif n<=15:
        return 640000
    elif n<=31:
        return 320000
    else:
        return 0



t = int(input())

for xx in range(t):
    a, b = map(int, input().split(' '))
    sumVal = 0
    sumVal += get2017(a)
    sumVal += get2018(b)
    print(sumVal)