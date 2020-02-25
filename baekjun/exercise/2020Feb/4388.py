# 받아올림
# https://www.acmicpc.net/problem/4388
# https://github.com/yhs3434

while True:
    a, b = map(int, input().split(' '))
    if a== 0 and b==0:
        break
    cnt = 0
    carry = 0

    while a > 0 and b > 0:
        if a%10 + b%10 + carry >= 10:
            carry = 1
            cnt += 1
        else:
            carry = 0
        a //= 10
        b //= 10
    while a%10 + b%10 + carry >= 10:
        cnt += 1
        a //= 10
        b //= 10
    print(cnt)