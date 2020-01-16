# 행렬 제곱
# https://www.acmicpc.net/problem/10830

def solution(a, b):

    cs = []

    while b > 0:
        c = [[a[i][j] for j in range(n)] for i in range(n)]
        cnt = 1
        while cnt*2 <= b:
            cnt *= 2
            c = matMul(c, c)
        b -= cnt
        cs.append(c)
    retMat = [[1 if i==j else 0 for i in range(n)] for j in range(n)]
    for css in cs:
        retMat = matMul(retMat, css)
    for xx in range(b):
        retMat = matMul(retMat, a)

    return retMat

def matMul(A, B):
    n = len(A)
    b = []
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(B[j][i])
        b.append(temp)
    for i in range(n):
        for j in range(n):
            C[i][j] = myMul(A[i], b[j])
    return C

def myMul(arr1, arr2):
    sumVal = 0
    for i in range(len(arr1)):
        sumVal += arr1[i]*arr2[i]
    return sumVal%1000

n, b = map(int, input().split(' '))
a = []
for xxx in range(n):
    a.append(list(map(int, input().split(' '))))
retMat = solution(a, b)
for row in retMat:
    for col in row:
        print(col, end=' ')
    print('')