# 연습문제 x만큼 간격이 있는 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    nx = 0
    while n > 0:
        n -= 1
        nx += x
        answer.append(nx)

    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))