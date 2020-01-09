# 분해합
# https://www.acmicpc.net/problem/2231

def solution(n):
    answer = 0

    for i in range(n//2, n):
        if splitAdd(i) == n:
            answer = i
            break

    return answer

def splitAdd(n):
    sumVal = n
    for x in str(n):
        sumVal += int(x)
    return sumVal

n = int(input())
print(solution(n))