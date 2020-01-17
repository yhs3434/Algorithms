# 농구 경기
# https://www.acmicpc.net/problem/1159
# https://github.com/yhs3434

myh = {}

n = int(input())
for xxx in range(n):
    p = input()
    if p[0] not in myh:
        myh[p[0]] = 1
    else:
        myh[p[0]] += 1
answer = []
for key in myh:
    if myh[key] >= 5:
        answer.append(key)
if answer:
    answer.sort()
    for a in answer:
        print(a, end='')
else:
    print('PREDAJA')