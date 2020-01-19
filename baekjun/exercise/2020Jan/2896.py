# 무알콜 칵테일
# https://www.acmicpc.net/problem/2896

a, b, c = map(int, input().split(' '))
x, y, z = map(int, input().split(' '))

p = a/x
q = b/y
r = c/z

minRate = min(p, q, r)

a -= x*minRate
b -= y*minRate
c -= z*minRate
print(a, b, c)