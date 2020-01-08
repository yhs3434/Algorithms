# 숫자의 합
# https://www.acmicpc.net/problem/11720

N = int(input())
nStr = input()
sumVal = 0
for n in nStr:
    sumVal += int(n)
print(sumVal)