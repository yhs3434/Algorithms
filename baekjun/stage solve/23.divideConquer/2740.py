# 행렬 곱셈
# https://www.acmicpc.net/problem/2740

def solution(a, b):
    for i in range(len(a)):
        for j in range(len(b[0])):
            arr1 = a[i]
            arr2 = []
            for k in range(len(b)):
                arr2.append(b[k][j])
            val = myMul(arr1, arr2)
            print(val, end=' ')
        print('')

    return

def myMul(arr1, arr2):
    sumVal = 0
    for i in range(len(arr1)):
        sumVal += arr1[i]*arr2[i]
    return sumVal

an, am = map(int, input().split(' '))
a = []
for xxx in range(an):
    a.append(list(map(int, input().split(' '))))
bn, bm = map(int, input().split(' '))
b = []
for xxx in range(bn):
    b.append(list(map(int, input().split(' '))))
solution(a, b)