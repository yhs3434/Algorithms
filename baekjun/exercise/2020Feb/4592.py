# 중복을 없애자
# https://www.acmicpc.net/problem/4592
# https://github.com/yhs3434/Algorithms

while True:
    n, *arr = map(int, input().split(' '))
    if n == 0:
        break

    bef = 0
    for a in arr:
        if a != bef:
            print(a, end=' ')
        bef = a
    print('$')