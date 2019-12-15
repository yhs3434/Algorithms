# 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048

def solution(w,h):
    answer = 0

    m = h/w
    curH = 0
    befH = 0
    for x in range(1,w+1):
        curH += m
        answer += amountGap(befH, curH)
        befH = curH

    return w*h-answer

def amountGap(x, y):
    x = int(x)
    if(int(y)==y):
        y=int(y)
    else:
        y=int(y)+1
    return y-x

print(solution(99999999,29999999))

