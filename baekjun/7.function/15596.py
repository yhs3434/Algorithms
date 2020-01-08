# 정수 N개의 합
# https://www.acmicpc.net/problem/15596

def solve(a: list):
    answer = 0

    for c in a:
        answer += c

    return answer

solve([1,2,3])