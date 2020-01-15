# 다리 놓기
# https://www.acmicpc.net/problem/1010

def solution(n, m):
    a = m
    b = n if (m-n) > n else m - n

    supVal = 1
    for i in range(b):
        supVal *= (a-i)
    subVal = 1
    for i in range(2, b+1):
        subVal *= i

    return supVal//subVal

t = int(input())
for xxx in range(t):
    n, m = map(int, input().split(' '))
    print(solution(n, m))