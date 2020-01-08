# 손익분기점
# https://www.acmicpc.net/problem/1712

def solution(a,b,c):
    if b>=c:
        return -1
    answer = 0

    stand = (a)/(c-b)
    answer = int(stand)+1

    return answer

a, b, c = map(int, input().split(' '))
print(solution(a,b,c))