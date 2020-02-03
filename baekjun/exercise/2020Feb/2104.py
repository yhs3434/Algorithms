# 부분배열 고르기
# https://www.acmicpc.net/problem/2104
# https://github.com/yhs3434/Algorithms

n = int(input())
arr = list(map(int, input().split(' ')))

answer = 0
for k in range(n):
    minVal = arr[k]
    i = k
    while i >= 0:
        if arr[i] >= minVal:
            i -= 1
        else:
            i += 1
            break
    if i < 0:
        i = 0
    j = k
    while j < n:
        if arr[j] >= minVal:
            j += 1
        else:
            j -= 1
            break
    if j >= n:
        j = n-1
    temp = arr[i:j+1]
    val = sum(temp)*minVal
    if val > answer:
        answer = val
print(answer)