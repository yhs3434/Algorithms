# Mini Fantasy War
# https://www.acmicpc.net/problem/12790
# https://github.com/yhs3434/Algorithms

t = int(input())
for xxx in range(t):
    a, b, c, d, e, f, g, h = map(int, input().split(' '))

    a += e
    b += f
    c += g
    d += h

    if a < 1:
        a = 1
    if b < 1:
        b = 1
    if c < 0:
        c = 0

    answer = a + 5*b + 2*c + 2*d
    print(answer)