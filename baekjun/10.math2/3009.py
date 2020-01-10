# 네 번째 점
# https://www.acmicpc.net/problem/3009

mhx = {}
mhy = {}

for xxx in range(3):
    x, y = map(int, input().split(' '))
    if x not in mhx:
        mhx[x] = 'x'
    else:
        del mhx[x]
    if y not in mhy:
        mhy[y] = 'y'
    else:
        del mhy[y]

print(list(mhx.keys())[0], list(mhy.keys())[0])