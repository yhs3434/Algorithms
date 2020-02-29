# 할로윈의 사탕
# https://www.acmicpc.net/problem/10178
# https://github.com/yhs3434/Algorithms

t = int(input())
for _ in range(t):
    a, b = map(int, input().split(' '))
    x = a//b
    y = a%b
    print('You get', x,'piece(s) and your dad gets',y,'piece(s).')