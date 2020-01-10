# 직사각형에서 탈출
# https://www.acmicpc.net/problem/1085

def getAbs(a, b):
    return a-b if a>b else b-a

x, y, w, h = map(int, input().split(' '))
answer = min(x, y, w-x, h-y)
print(answer)