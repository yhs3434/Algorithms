# 서머코딩/윈터코딩(~2018) 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0

    d.sort()
    cnt = 0
    for dd in d:
        budget -= dd
        if budget < 0:
            break
        else:
            cnt += 1
    answer = cnt
    return answer

print(solution([1,3,2,5,4], 9))