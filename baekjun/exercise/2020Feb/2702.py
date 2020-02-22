# 초6 수학
# https://www.acmicpc.net/problem/2702
# https://github.com/yhs3434/Algorithms

def getGCD(a,b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
for _ in range(n):
    a, b = map(int, input().split(' '))
    gcdd = getGCD(a, b)
    print(a*b//gcdd, gcdd)