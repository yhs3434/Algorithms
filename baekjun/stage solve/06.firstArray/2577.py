# 숫자의 개수
# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

res = a*b*c
lenR = len(str(res))
cnt = [0 for i in range(10)]
for i in range(lenR-1, -1, -1):
    c = res//(10**i)
    res %= (10**i)
    cnt[c] += 1
for c in cnt:
    print(c)