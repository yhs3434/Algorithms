# 지영 공주님의 마법 거울
# https://www.acmicpc.net/problem/11586

n = int(input())
mirror = []
for xxx in range(n):
    mirror.append(input())
k = int(input())

if k==1:
    for m in mirror:
        print(m)
elif k==2:
    for i in range(n):
        for j in range(n-1, -1, -1):
            print(mirror[i][j], end='')
        print('')
elif k==3:
    for i in range(n-1, -1, -1):
        for j in range(n):
            print(mirror[i][j], end='')
        print('')