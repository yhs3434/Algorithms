# 중간계 전쟁
# https://www.acmicpc.net/problem/4435
# https://github.com/yhs3434/Algorithms

t = int(input())

for _ in range(t):
    arr1 = list(map(int, input().split(' ')))
    arr2 = list(map(int, input().split(' ')))

    val1 = arr1[0] + 2*arr1[1] + 3*arr1[2] + 3*arr1[3] + 4*arr1[4] + 10*arr1[5]
    val2 = arr2[0] + 2*arr2[1] + 2*arr2[2] + 2*arr2[3] + 3*arr2[4] + 5*arr2[5] + 10*arr2[6]

    print('Battle '+str(_+1)+':', end=' ')
    if val1 > val2:
        print('Good triumphs over Evil')
    elif val1 < val2:
        print('Evil eradicates all trace of Good')
    else:
        print('No victor on this battle field')