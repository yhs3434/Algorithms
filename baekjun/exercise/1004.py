# 어린 왕자
# https://www.acmicpc.net/problem/1004

def getDist(x, y):
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**(1/2)

t = int(input())
for xxx in range(t):
    sx, sy, ex, ey = map(int, input().split(' '))
    n = int(input())
    stars = []
    for i in range(n):
        stars.append(list(map(int, input().split(' '))))
    cnt = 0
    for star in stars:
        if getDist((sx,sy), (star[0],star[1])) < star[2] or getDist((ex,ey), (star[0],star[1])) < star[2]:
            if getDist((sx,sy), (star[0],star[1])) < star[2] and getDist((ex,ey), (star[0],star[1])) < star[2]:
                continue
            else:
                cnt += 1
    print(cnt)
