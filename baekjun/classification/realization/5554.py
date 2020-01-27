# 심부름 가는 길
# https://www.acmicpc.net/problem/5554
# https://github.com/yhs3434/Algorithms

a = int(input())
b = int(input())
c = int(input())
d = int(input())

time = a+b+c+d
m = time//60
s = time%60
print(m)
print(s)