# 돌 게임
# https://www.acmicpc.net/problem/9655
# https://github.com/yhs3434/Algorithms

n = int(input())
n %= 4

if n==0:
    print('CY')
elif n==1:
    print('SK')
elif n==2:
    print('CY')
else:
    print('SK')