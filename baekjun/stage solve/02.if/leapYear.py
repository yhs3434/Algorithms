# 윤년
# https://www.acmicpc.net/problem/2753

y = int(input())

if y%400==0:
    print(1)
else:
    if y%100!=0 and y%4==0:
        print(1)
    else:
        print(0)