# 터널의 입구와 출구
# https://www.acmicpc.net/problem/5612
# https://github.com/yhs3434/Algorithms

n = int(input())
m = int(input())
answer = 0
flag = False
for _ in range(n):
    a, b = map(int, input().split(' '))
    m = m + a - b
    if m < 0:
        flag = True
        break
    if m > answer:
        answer = m
if flag:
    print(0)
else:
    print(answer)