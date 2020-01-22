# 최대공약수
# https://www.acmicpc.net/problem/1850
# https://github.com/yhs3434/Algorithms

def getGCD(a,b):
    while b > 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split(' '))
gcdd = getGCD(a, b)
print('1'*gcdd)