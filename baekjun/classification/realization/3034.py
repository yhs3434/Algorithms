# 앵그리 창영
# https://www.acmicpc.net/problem/3034
# https://github.com/yhs3434/Algorithms

N, W, H = map(int, input().split(' '))
std = (W**2 + H**2)**0.5
for _ in range(N):
    n = int(input())
    if n <= std:
        print('DA')
    else:
        print('NE')