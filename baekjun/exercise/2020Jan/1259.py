# 팰린드롬수
# https://www.acmicpc.net/problem/1259

while True:
    n = input()
    if n == '0':
        break
    i = 0
    j = len(n) - 1

    flag = True
    while i<=j:
        if n[i] != n[j]:
            flag = False
            break
        else:
            i += 1
            j -= 1
    if flag:
        print('yes')
    else:
        print('no')