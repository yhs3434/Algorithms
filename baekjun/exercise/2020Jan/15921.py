# 수찬은 마린보이야!!
# https://www.acmicpc.net/problem/15921
# https://github.com/yhs3434/Algorithms

n = int(input())
if n==0:
    print('divide by zero')
else:
    arr = list(map(int, input().split(' ')))
    avg = sum(arr)/n
    exp = sum(arr)/n
    print('%.2f'%1.00)