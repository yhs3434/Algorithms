# 아름다운 수
# https://www.acmicpc.net/problem/2774

t = int(input())
for _ in range(t):
    x = input()
    sett = set()
    for c in x:
        sett.add(c)
    print(len(sett))