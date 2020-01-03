# 연습문제 - 최고의 집합
# https://programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    answer = []

    if s/n < 1:
        answer = [-1]
    elif s/n == int(s/n):
        answer = [s//n for i in range(n)]
    else:
        answer = [s//n for i in range(n)]
        s -= ((s//n)*n)
        i = 0
        while s > 0:
            answer[i] += 1
            i = (i + 1)%n
            s -= 1
        answer.sort()

    return answer

print(solution(2, 8))
print(solution(2, 9))