# 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []

    bef = ''
    for i in range(len(arr)):
        cur = arr[i]
        if(bef != cur):
            answer.append(cur)
        bef = cur

    return answer

print(solution([1,1,3,3,0,1,1]))