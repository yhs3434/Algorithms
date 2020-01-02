# 서머코딩 / 윈터코딩 (~2018) - 점프와 순간 이동
# https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    answer = 0

    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            answer += 1
            n -= 1

    return answer

print(solution(5))
print(solution(6))
print(solution(5000))
