# 연습문제 - 짝수와 홀수
# https://programmers.co.kr/learn/courses/30/lessons/12937

def solution(num):
    answer = ''

    if num%2==0:
        answer = 'Even'
    else:
        answer = 'Odd'

    return answer

print(solution(3))