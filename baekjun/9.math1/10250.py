# ACM 호텔
# https://www.acmicpc.net/problem/10250

def solution(h, w, n):
    answer = 0

    room = 101

    while n>1:
        if room//100 < h:
            room += 100
        else:
            room = 100 + room%100 + 1
        n -= 1
    answer = room

    return answer

t = int(input())

for xxx in range(t):
    h, w, n = map(int, input().split(' '))
    print(solution(h, w, n))