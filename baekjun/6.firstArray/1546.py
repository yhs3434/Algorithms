# 평균
# https://www.acmicpc.net/problem/1546

n = int(input())
scores = list(map(int, input().split(' ')))
maxScore = max(scores)
sumVal = 0
for s in scores:
    newScore = s/maxScore*100
    sumVal += newScore
print(sumVal/n)