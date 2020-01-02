# 연습문제 - 최댓값과 최솟값
# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''

    arr = list(map(int, s.split(' ')))
    answer = str(min(arr)) + ' ' + str(max(arr))

    return answer

print(solution("-1 -2 -3 -4"))