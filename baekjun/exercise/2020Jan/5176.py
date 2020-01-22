# 대회 자리
# https://www.acmicpc.net/problem/5176
# https://github.com/yhs3434

t = int(input())
for xxx in range(t):
    p, m = map(int, input().split(' '))
    seats = []
    for i in range(p):
        seats.append(int(input()))
    visited = [False] * (m+1)
    cnt = 0
    for s in seats:
        if visited[s]:
            cnt += 1
        else:
            visited[s] = True
    print(cnt)