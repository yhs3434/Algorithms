# 별 찍기 - 10
# https://www.acmicpc.net/problem/2447

def makeEmpty(n):
    for i in range(n):
        print(' ', end='')
    return

def makeStar(n, r):
    if n == 1:
        print('*', end='')
    else:
        if (r/n) < (1/3):
            if r%3 == 0:
                for i in range(3):
                    makeStar(n//3, r%(n//3))
            elif r%3 == 1:
                for i in range(3):
                    makeStar(n // 3, r %(n//3))
            else:
                for i in range(3):
                    makeStar(n//3, r%(n//3))
        elif (r/n) < (2/3):
            if r % 3 == 0:
                makeStar(n // 3, r % (n//3))
                makeEmpty(n // 3)
                makeStar(n // 3, r % (n//3))
            elif r % 3 == 1:
                makeStar(n // 3, r % (n//3))
                makeEmpty(n // 3)
                makeStar(n // 3, r % (n//3))
            else:
                makeStar(n // 3, r % (n//3))
                makeEmpty(n // 3)
                makeStar(n // 3, r % (n//3))
        else:
            if r%3 == 0:
                for i in range(3):
                    makeStar(n//3, r%(n//3))
            elif r%3 == 1:
                for i in range(3):
                    makeStar(n // 3, r % (n//3))
            else:
                for i in range(3):
                    makeStar(n//3, r%(n//3))

N = int(input())

for i in range(N):
    makeStar(N, i)
    print('')