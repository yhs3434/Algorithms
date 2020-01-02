# 연습문제 - 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []

    measure = 0
    multiple = 0
    a = n
    b = m

    while n != m:
        subVal = getSub(n, m)
        if n>m:
            n = subVal
        else:
            m = subVal

    measure = n
    multiple = (a//n)*(b//n)*n
    answer = [measure, multiple]
    return answer

def getSub(n1, n2):
    return n1 - n2 if n1 - n2 > 0 else n2 - n1

print(solution(3, 12))