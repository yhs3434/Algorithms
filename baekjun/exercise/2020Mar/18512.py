# 점프 점프
# https://www.acmicpc.net/problem/18512
# https://github.com/yhs3434/Algorithms

x, y, p1, p2 = map(int, input().split(' '))

a, b = p1, p2

while a != b and a<100000:
    if a < b:
        a += x
    else:
        b += y
print(a) if a < 100000 else print(-1)