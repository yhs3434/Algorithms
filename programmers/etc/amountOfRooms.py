# 방의 개수
# https://programmers.co.kr/learn/courses/30/lessons/49190

def solution(arrows):
    answer = 0

    dots = set()
    lines = set()
    cur = (0, 0)
    before = cur
    dots.add(cur)
    for a in arrows:
        for i in range(2):
            cur = move(a, before)
            dots.add(cur)
            if cur > before:
                lines.add((before, cur))
            else:
                lines.add((cur, before))
            before = cur
    answer = len(lines) - len(dots) + 1
    return answer

def move(n, position):
    x = position[0]
    y = position[1]
    p = 0
    if (n==0):
        p = (x, y+1)
    elif (n==1):
        p = (x+1, y+1)
    elif (n==2):
        p = (x+1, y)
    elif (n==3):
        p = (x+1, y-1)
    elif (n==4):
        p = (x, y-1)
    elif (n==5):
        p = (x-1, y-1)
    elif (n==6):
        p = (x-1, y)
    elif (n==7):
        p = (x-1, y+1)
    return p

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 6, 2, 1, 6, 5, 5, 3, 6, 0]))