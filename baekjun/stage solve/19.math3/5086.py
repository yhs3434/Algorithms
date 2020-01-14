# 배수와 약수
# https://www.acmicpc.net/problem/5086

def solution(a, b):
    if b % a == 0:
        return 'factor'
    elif a % b == 0:
        return 'multiple'
    else:
        return 'neither'

while True:
    a, b = map(int, input().split(' '))
    if a==0 and b==0:
        break
    print(solution(a, b))