# 영화감독 숌
# https://www.acmicpc.net/problem/1436

def solution(n):
    answer = 0

    num = 665
    cnt = 0
    while cnt < n:
        num += 1
        if isDevil(num):
            answer = num
            cnt += 1

    return answer

def isDevil(n):
    while n>=666:
        if n%1000 == 666:
            return True
        n //= 10
    return False

n = int(input())
print(solution(n))