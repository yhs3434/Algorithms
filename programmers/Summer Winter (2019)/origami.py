# 서머코딩 / 윈터코딩 (2019) - 종이접기
# https://programmers.co.kr/learn/courses/30/lessons/62049?language=python3

def solution(n):
    answer = [0]

    while n>1:
        alen = len(answer)
        flag = True
        flag2 = 0
        newAnswer = [0]
        i = 0
        while i<alen:
            if flag:
                newAnswer.append(answer[i])
                i += 1
                flag = False
            else:
                flag2 = (flag2 + 1) % 2
                newAnswer.append(flag2)
                flag = True
        newAnswer.append(1)
        answer = newAnswer
        n-=1
    return answer

print(solution(3))