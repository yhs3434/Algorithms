# 연습문제 - 피보나치 수
# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = 0

    F = [0 for i in range(n+1)]
    F[1] = 1

    for i in range(2, n+1):
        F[i] = F[i-2] + F[i-1]
    answer = F[-1]

    return answer%1234567

print(solution(5))