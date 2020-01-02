# 연습문제 - 콜라츠 추측
# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0

    while num!=1 and answer<500:
        if isEven(num):
            num //= 2
        else:
            num = num*3 + 1
        answer += 1
    if num!=1:
        answer = -1
    return answer

def isEven(num):
    return True if num%2==0 else False

print(solution(626331))