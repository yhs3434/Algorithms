# 돌 게임 2
# https://www.acmicpc.net/problem/9656
# https://github.com/yhs3434/Algorithms

n = int(input())
n %= 4

if n==0:
    print('SK')
elif n==1:
    print('CY')
elif n==2:
    print('SK')
else:
    print('CY')