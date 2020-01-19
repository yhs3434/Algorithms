# 럭비 클럽
# https://www.acmicpc.net/problem/2083

while True:
    name, a, b = input().split(' ')
    a = int(a)
    b = int(b)
    if name=='#':
        break

    if a > 17 or b >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')