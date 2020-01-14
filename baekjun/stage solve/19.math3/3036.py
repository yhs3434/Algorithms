# 링
# https://www.acmicpc.net/problem/3036

def getGCD(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(rings):
    fRing = rings[0]

    for i in range(1, len(rings)):
        cRing = rings[i]
        gcdd = getGCD(fRing, cRing)
        print(str(fRing//gcdd)+'/'+str(cRing//gcdd))

n = int(input())
rings = list(map(int, input().split(' ')))
solution(rings)