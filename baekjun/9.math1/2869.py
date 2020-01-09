# 달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869

a, b, v = map(int, input().split(' '))

x = (v-a)/(a-b)
if x==int(x):
    print(int(x)+1)
else:
    print(int(x)+2)