# Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011

def solution(x, y):
    answer = 0

    n = y-x
    i = 1
    j = 1
    while n>0:
        answer += 1
        if i==j:
            n -= i
            i += 1
        else:
            n -= j
            j += 1

    return answer

t = int(input())
for xxx in range(t):
    x, y = map(int, input().split(' '))
    print(solution(x, y))