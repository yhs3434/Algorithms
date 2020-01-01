# 연습문제 2 x n 타일링
# https://programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    answer = 0

    if n<3:
        return n
    bb = 1
    b = 2
    c = 3

    for i in range(3, n+1):
        c = bb + b
        bb = b
        b = c
    answer = c

    return answer%1000000007

print(solution(7))