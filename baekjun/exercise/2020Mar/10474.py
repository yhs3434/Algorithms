# 분수좋아해?
# https://www.acmicpc.net/problem/10474

while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break

    x = a//b
    a %= b
    print(x,a,'/',b)