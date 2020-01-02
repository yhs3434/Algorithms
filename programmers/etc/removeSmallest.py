# 연습문제 - 제일 작은 수 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    answer = []

    arr.remove(min(arr))
    if arr == []:
        answer = [-1]
    else:
        answer = arr

    return answer

print(solution([4,3,2,1]))