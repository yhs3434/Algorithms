# 거스름돈
# https://www.acmicpc.net/problem/5585

moneys = [1, 5, 10, 50, 100, 500]

n = int(input())

cur = 1000 - n
cnt = 0
while cur > 0:
    money = moneys.pop()
    cnt += (cur//money)
    cur %= money
print(cnt)