# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0

    temp = []
    for i in range(len(lost)):
        l = lost[i]
        if(l in reserve):
            reserve.remove(l)
            temp.append(l)
    for t in temp:
        lost.remove(t)

    count = 0
    for l in lost:
        if((l-1) in reserve):
            reserve.remove(l-1)
            count += 1
        elif((l+1) in reserve):
            reserve.remove(l+1)
            count += 1

    answer = n - (len(lost)-count)

    return answer

print(solution(5, [2,4], [1,3,5]))