# 경로 찾기
# https://www.acmicpc.net/problem/11403
# https://github.com/yhs3434/Algorithms

n = int(input())
dist = [[float('inf')]*n for _ in range(n)]
for i in range(n):
    inp = list(map(int, input().split(' ')))
    for j in range(n):
        if inp[j] == 1:
            dist[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(n):
    for j in range(n):
        if dist[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(1, end=' ')
    print('')