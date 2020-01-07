# OX퀴즈
# https://www.acmicpc.net/problem/8958

n = int(input())
for xxx in range(n):
    ox = input()
    cnt = 0
    sumVal = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            cnt += 1
            sumVal += cnt
        else:
            cnt = 0
    print(sumVal)