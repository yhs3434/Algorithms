# J박스
# https://www.acmicpc.net/problem/5354
# https://github.com/yhs3434/Algorithms

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        for j in range(n):
            if i==0 or i==(n-1) or j==0 or j==(n-1):
                print('#', end='')
            else:
                print('J', end='')
        print('')
    print('')