# 직사각형 네개의 합집합의 면적 구하기
# https://www.acmicpc.net/problem/2669
# https://github.com/yhs3434/Algorithms

rect = {}

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split(' '))
    for i in range(x1, x2):
        for j in range(y1, y2):
            if i not in rect:
                rect[i] = {}
            rect[i][j] = True

cnt = 0
for i in rect:
    for j in rect[i]:
        cnt += 1
print(cnt)