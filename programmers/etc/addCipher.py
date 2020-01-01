# 연습문제 - 자릿수 더하기
# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0

    while n>0:
        answer += n // (10**(len(str(n))-1))
        n %= (10**(len(str(n))-1))

    return answer

print(solution(123))