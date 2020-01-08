# 문자열 반복
# https://www.acmicpc.net/problem/2675

T = int(input())

for xxx in range(T):
    cline = input().split(' ')
    n = int(cline[0])
    strr = cline[1]
    for l in strr:
        print(l*n, end='')
    print('')