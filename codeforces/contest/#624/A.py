import sys
rl = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, rl().rstrip().split(' '))
    if a == b:
        print(0)
    else:
        if a < b:
            if (b-a)%2 == 0:
                print(2)
            else:
                print(1)
        else:
            if (a-b)%2 == 0:
                print(1)
            else:
                print(2)