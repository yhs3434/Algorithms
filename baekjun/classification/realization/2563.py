# 색종이
# https://www.acmicpc.net/problem/2563
# https://github.com/yhs3434/Algorithms

board = [[0] * 100 for i in range(100)]

n = int(input())
for xxx in range(n):
    x, y = map(int, input().split(' '))
    for i in range(10):
        for j in range(10):
            board[y+i][x+j] = 1
answer = 0
for i in range(100):
    answer += board[i].count(1)
print(answer)