# 연습문제 - 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True
    temp = []
    a = x
    lenX = len(str(x)) - 1
    while lenX>=0:
        temp.append(a//(10**lenX))
        a %= (10**lenX)
        lenX -= 1

    if x/sum(temp) == int(x/sum(temp)):
        return True
    else:
        return False

    return answer

print(solution(12))