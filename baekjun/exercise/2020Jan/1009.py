# 분산처리
# https://www.acmicpc.net/problem/1009

t = int(input())
for xxx in range(t):
    a, b = map(int, input().split(' '))

    ns = []

    while b > 1:
        n = 1
        x = a
        while n*2 <= b:
            x = (x*x) % 10
            n *= 2
        b -= n
        ns.append(x)
    answer = 1
    for i in range(b):
        answer *= a
    for n in ns:
        answer = (answer * n) % 10
    answer = answer % 10
    if answer == 0:
        answer = 10
    print(answer)
