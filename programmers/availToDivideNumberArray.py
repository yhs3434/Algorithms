# 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []

    for i in range(len(arr)):
        if(arr[i]%divisor==0):
            answer.append(arr[i])
    if(len(answer)==0):
        return [-1]
    answer.sort()

    return answer