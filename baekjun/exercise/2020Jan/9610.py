# 사분면
# https://www.acmicpc.net/problem/9610
# https://github.com/yhs3434/Algorithms

cnts = [0, 0, 0, 0, 0]

t = int(input())
for xxx in range(t):
    x, y = map(int, input().split(' '))

    if x == 0 or y == 0:
        cnts[4] += 1
    elif x > 0 and y > 0:
        cnts[0] += 1
    elif x < 0 and y > 0:
        cnts[1] += 1
    elif x < 0 and y < 0:
        cnts[2] += 1
    elif x > 0 and y < 0:
        cnts[3] += 1
print('Q1:', cnts[0])
print('Q2:', cnts[1])
print('Q3:', cnts[2])
print('Q4:', cnts[3])
print('AXIS:', cnts[4])