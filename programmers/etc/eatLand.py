# 연습문제 - 땅따먹기
# https://programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    answer = max(land[-1])
    return answer


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
#print(solution([[1,2,3,5]]))