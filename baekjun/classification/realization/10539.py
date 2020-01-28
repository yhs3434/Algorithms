# 수빈이와 수열
# https://www.acmicpc.net/problem/10539
# https://github.com/yhs3434/Algorithms

n = int(input())
b = list(map(int, input().split(' ')))

a = [0] * len(b)
a[0] = b[0]
for i in range(1, len(b)):
    a[i] = (i+1)*b[i] - (i)*b[i-1]
for x in a:
    print(x, end=' ')
