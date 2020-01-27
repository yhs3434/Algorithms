# 방학 숙제
# https://www.acmicpc.net/problem/5532
# https://github.com/yhs3434/Algorithms

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = a//c
if a//c != a/c:
    x += 1
y = b//d
if b//d != b/d:
    y += 1
val = max(x, y)
print(l - val)