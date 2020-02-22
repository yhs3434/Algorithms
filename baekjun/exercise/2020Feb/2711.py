# 오타맨 고창영
# https://www.acmicpc.net/problem/2711
# https://github.com/yhs3434/Algorithms

T = int(input())
for _ in range(T):
    a, b = input().split(' ')
    a = int(a)-1
    print(b[:a]+b[a+1:])