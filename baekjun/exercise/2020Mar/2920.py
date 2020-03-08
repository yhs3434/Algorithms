# 음계
# https://www.acmicpc.net/problem/2920

arr = list(map(int, input().split()))
flaga = True
flagd = True
bef = 0
for i in range(len(arr)):
    if i==0:
        bef = arr[i]
    else:
        if arr[i] <= bef:
            flaga = False
        elif arr[i] >= bef:
            flagd = False
        bef = arr[i]

if flaga:
    print('ascending')
elif flagd:
    print('descending')
else:
    print('mixed')