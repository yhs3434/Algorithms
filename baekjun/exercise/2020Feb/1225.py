# 이상한 곱셈
# https://www.acmicpc.net/problem/1225
# https://github.com/yhs3434/Algorithms

a, b = input().split(' ')
a = list(map(int, list(a)))
b = list(map(int, list(b)))

lena = len(a)
lenb = len(b)
val = 0
for i in range(lena):
    for j in range(lenb):
        val += a[i]*b[j]
print(val)