# 문자열
# https://www.acmicpc.net/problem/1120
# https://github.com/yhs3434/Algorithms

a, b = input().split(' ')

lena = len(a)
lenb = len(b)

answer = float('inf')
for i in range(lenb - lena + 1):
    cb = b[i:]
    cnt = 0
    for j in range(lena):
        if cnt >= answer:
            break
        if a[j] != cb[j]:
            cnt += 1
    if cnt < answer:
        answer = cnt
print(answer)