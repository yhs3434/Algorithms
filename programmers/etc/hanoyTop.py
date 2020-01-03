# 연습문제 - 하노이 탑
# https://programmers.co.kr/learn/courses/30/lessons/12946

def solution(n):
    answer = []

    hanoi(n, 1, 2, 3, answer)

    return answer

def moveTo(f, t, answer):
    answer.append([f, t])

def hanoi(n, f, b, t, answer):
    if n == 1:
        moveTo(f, t, answer)
    else:
        hanoi(n-1, f, t, b, answer)
        moveTo(f, t, answer)
        hanoi(n-1, b, f, t, answer)

print(solution(3))