from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split(' ')))

    if sum(arr)%2 == 1:
        print('YES')
    else:
        count = [0, 0]
        newArr = list(set(arr))
        for a in newArr:
            if a%2==1:
                count[0] += 1
            else:
                count[1] += 1
            if count[0]>0 and count[1]>0:
                break
        if count[0] > 0 and count[1] > 0:
            print('YES')
        else:
            print('NO')