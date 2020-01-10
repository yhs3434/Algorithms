# 직각삼각형
# https://www.acmicpc.net/problem/4153

while True:
    x, y, z = map(int, input().split(' '))
    if x==0 and y==0 and z==0:
        break
    pos = [x, y, z]
    pos.sort()
    if pos[0]**2 + pos[1]**2 == pos[2]**2:
        print('right')
    else:
        print('wrong')
