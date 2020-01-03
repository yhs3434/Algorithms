# 연습문제 - 줄 서는 방법
# https://programmers.co.kr/learn/courses/30/lessons/12936

def solution(n, k):
    answer = []
    people = [i+1 for i in range(n)]
    answer = getKth(people, k-1)

    return answer

def getKth(arr, k):
    if len(arr) == 1:
        return arr
    lenA = len(arr)
    caseN = getCases(arr)
    idx = k // (caseN//lenA)
    return [arr[idx]] + getKth(arr[:idx] + arr[idx+1:], k % (caseN//lenA))

def getCases(arr):
    answer = 1
    for i in range(2, len(arr)+1):
        answer *= i
    return answer

print(solution(3, 5))