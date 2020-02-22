# 주사위
# https://www.acmicpc.net/problem/9295
# https://github.com/yhs3434/Algorithms

T = int(input())
for _ in range(T):
    a, b = map(int, input().split(' '))
    print('Case', str(_+1)+':', a+b)