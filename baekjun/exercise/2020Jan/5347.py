# LCM
# https://www.acmicpc.net/problem/5347
# https://github.com/yhs3434

def getGCD(a,b):
    while b > 0:
        a, b = b, a % b
    return a

t = int(input())
for xxx in range(t):
    a, b = map(int, input().split(' '))
    gcdd = getGCD(a, b)
    print(a*b//gcdd)