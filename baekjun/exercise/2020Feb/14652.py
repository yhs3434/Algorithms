# 나는 행복합니다~
# https://www.acmicpc.net/problem/14652
# https://github.com/yhs3434/Algorithms

n, m, k = map(int,input().split(' '))

answer = [0, 0]
answer[0] += k//m
k %= m
answer[1] += k
print(answer[0], answer[1])