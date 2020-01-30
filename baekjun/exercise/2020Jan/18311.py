# 왕복
# https://www.acmicpc.net/problem/18311
# https://github.com/yhs3434/Algorithms

def getIdx(arr, val):
    left = 0
    right = len(arr) - 1
    idx = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= val:
            left = mid + 1
            if mid > idx:
                idx = mid
        else:
            right = mid - 1
    return idx

N, K = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))


val = 0
cnt = 0
i = 0
flag = True
if len(arr) == 1:
    flag = False
else:
    flag = True
flag2 = True
while True:
    cnt += 1
    val += arr[i]
    if val > K:
        break
    if flag:
        i += 1
        if i == len(arr) - 1:
            flag = False
    else:
        if flag2:
            flag2 = False
        else:
            i -= 1

if cnt <= N:
    print(cnt)
else:
    print(N - (cnt-N) + 1)