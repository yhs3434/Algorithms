# 평균은 넘겠지
# https://www.acmicpc.net/problem/4344

n = int(input())

for xxx in range(n):
    scores = list(map(int, input().split(' ')))
    pn = scores.pop(0)
    meanVal = sum(scores)/pn
    cnt = 0
    for s in scores:
        if s>meanVal:
            cnt += 1
    perStr = str(round(cnt/pn*100,3))
    sosuStr = perStr.split('.')[1]
    perStr += '0'*(3-len(sosuStr))
    print(perStr+'%')