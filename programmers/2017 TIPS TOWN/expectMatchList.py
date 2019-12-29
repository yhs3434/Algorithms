# 2017 팁스타운 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 0

    a += (n-1)
    b += (n-1)

    while a != b:
        a //= 2
        b //= 2
        answer += 1

    return answer

print(solution(8, 4, 7))