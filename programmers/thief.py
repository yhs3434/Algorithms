# 도둑질
# https://programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    answer = 0

    length = len(money)
    if (length == 3):
        answer = max(money)
        return answer

    start0 = [0 for i in range(length)]
    start1 = start0[:]
    start2 = start0[:]

    start0[0] = money[0]
    start0[2] = money[0] + money[2]
    start1[1] = money[1]
    start1[3] = money[1] + money[3]
    start2[2] = money[2]

    for i in range(2, len(money)-1):
        if(i==2):
            start0[i] = start0[i-2] + money[i]
        else:
            start0[i] = max(start0[i-3], start0[i-2]) + money[i]
    for i in range(3, len(money)):
        if(i==3):
            start1[i] = start1[i-2] + money[i]
        else:
            start1[i] = max(start1[i-3], start1[i-2]) + money[i]
    for i in range(4, length):
        start2[i] = max(start2[i-3], start2[i-2]) + money[i]
    answer = max([start0[-3], start0[-2], start1[-2], start1[-1], start2[-1]])
    return answer

print(solution([1,2,3,1,1,2,3,1,1,2,3,1]))