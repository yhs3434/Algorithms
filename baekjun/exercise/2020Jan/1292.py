# 쉽게 푸는 문제
# https://www.acmicpc.net/problem/1292

a, b = map(int, input().split(' '))

arr = [0] * 1001
j = 1
flag = False
for i in range(1, 500):
    if flag:
        break
    cnt = i
    while cnt > 0:
        if j > b:
            flag = True
            break
        arr[j] = i
        j += 1
        cnt -= 1
print(sum(arr[a:b+1]))