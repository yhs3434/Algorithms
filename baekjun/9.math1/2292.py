# 벌집
# https://www.acmicpc.net/problem/2292

def solution(n):
    answer = 1
    a = 1
    mul = 6
    while n>a:
        answer += 1
        a += mul
        mul += 6
    return answer

n = int(input())
print(solution(n))