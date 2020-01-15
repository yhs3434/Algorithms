# 검증수
# https://www.acmicpc.net/problem/2475

arr = list(map(int, input().split(' ')))
sumVal = 0
for a in arr:
    sumVal += a**2
print(sumVal%10)