# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

n = int(input())
pos = []
for xxx in range(n):
    pos.append(tuple(map(int, input().split(' '))))
pos.sort(key=lambda key: key[1])
pos.sort(key=lambda key: key[0])
for p in pos:
    print(p[0],p[1])