# 연습문제 - 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = ''

    temp = []
    lenN = len(str(n)) - 1
    while lenN >= 0:
        temp.append(n // (10 ** lenN))
        n %= (10 ** lenN)
        lenN -= 1

    temp.sort(reverse=True)
    for t in temp:
        answer += str(t)
    answer = int(answer)

    return answer

print(solution(118372))