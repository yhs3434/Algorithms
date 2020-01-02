# 연습문제 - 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0

    for i in range(1, n//2+1):
        if isAvail(n, n/i, i):
            answer += 1

    return answer

def isAvail(n, x, vol):
    if vol%2 == 0:
        if x - int(x) == 0.5:
            if int(x) - (vol//2 -1) > 0:
                return True
    else:
        if x == int(x):
            if int(x) - vol//2 > 0:
                return True
    return False

print(solution(15))