# 욱제는 건축왕이야!!
# https://www.acmicpc.net/problem/15923
# https://github.com/yhs3434/Algorithms

n = int(input())
maxX = -float('inf')
maxY = -float('inf')
minX = float('inf')
minY = float('inf')

for _ in range(n):
    x, y = map(int, input().split(' '))
    if x > maxX:
        maxX = x
    if y > maxY:
        maxY = y
    if x < minX:
        minX = x
    if y < minY:
        minY = y
print(2*(maxX-minX+maxY-minY))