# 분수 합
# https://www.acmicpc.net/problem/1735
# https://github.com/yhs3434/Algorithms

def getGCD(a,b):
    while b > 0:
        a, b = b, a % b
    return a

a1, b1 = map(int, input().split(' '))
a2, b2 = map(int, input().split(' '))

sub = b1*b2
sup = a1*b2 + a2*b1

gcdd = getGCD(sub, sup)
print(sup//gcdd, sub//gcdd)