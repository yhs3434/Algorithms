# 고층 건물
# https://www.acmicpc.net/problem/1027
# https://github.com/yhs3434/Algorithms

N = int(input())
arr = list(map(int, input().split(' ')))

answer = 0
for i in range(N):
    cnt = 0
    for j in range(i):
        flag = False
        m = (arr[i] - arr[j])/(i - j)
        b = arr[j] - m*j
        for k in range(j+1, i):
            if m*k + b <= arr[k]:
                flag = True
                break
        if not flag:
            cnt += 1
    for j in range(i+1, N):
        flag = False
        m = (arr[j] - arr[i])/(j-i)
        b = arr[i] - m*i
        for k in range(i+1, j):
            if m*k + b <= arr[k]:
                flag = True
                break
        if not flag:
            cnt += 1

    if cnt > answer:
        answer = cnt
print(answer)