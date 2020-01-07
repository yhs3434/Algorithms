# 음계
# https://www.acmicpc.net/problem/2920

arr = list(map(int,input().split(' ')))
af = True
df = True
before = 0
for a in arr:
    if before==0:
        before = a
    else:
        if a < before:
            af = False
        if a > before:
            df = False
        before = a
if af:
    print('ascending')
elif df:
    print('descending')
else:
    print('mixed')