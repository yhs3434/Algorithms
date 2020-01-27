# 수도요금
# https://www.acmicpc.net/problem/10707
# https://github.com/yhs3434/Algorithms

a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

x = p*a
y = b
if p - c > 0:
    y += d * (p - c)
print(min(x,y))