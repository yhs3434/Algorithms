# 소트인사이드
# https://www.acmicpc.net/problem/1427

num = input()
numArr = []
for n in num:
    numArr.append(int(n))
numArr.sort(reverse=True)
for n in numArr:
    print(n, end='')