# 오븐 시계
# https://www.acmicpc.net/problem/2525
# https://github.com/yhs3434

a, b = map(int, input().split(' '))
c = int(input())

b += c
h = b // 60
b %= 60

a += h
a %= 24

print(a, b)