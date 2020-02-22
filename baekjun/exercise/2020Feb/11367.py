# Report Card Time
# https://www.acmicpc.net/problem/11367
# https://github.com/yhs3434/Algorithms

T = int(input())
for _ in range(T):
    a, b = input().split(' ')
    b = int(b)

    print(a, end=' ')

    if b>=97:
        print('A+')
    elif b>=90:
        print('A')
    elif b>=87:
        print('B+')
    elif b>=80:
        print('B')
    elif b>=77:
        print('C+')
    elif b>=70:
        print('C')
    elif b>=67:
        print('D+')
    elif b>=60:
        print('D')
    else:
        print('F')