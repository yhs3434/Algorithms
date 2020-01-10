# 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651

n = int(input())
pos = []
for xxx in range(n):
    pos.append(tuple(map(int, input().split(' '))))
pos.sort(key=lambda key: key[0])
pos.sort(key=lambda key: key[1])
for p in pos:
    print(p[0],p[1])