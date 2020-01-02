# 연습문제 - 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    answer = 0

    if int(n**(1/2)) == n**(1/2):
        answer = (int(n**(1/2))+1)**2
    else:
        answer = -1

    return answer

print(solution(121))