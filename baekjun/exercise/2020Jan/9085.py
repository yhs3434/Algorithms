# 더하기
# https://www.acmicpc.net/problem/9085
# https://github.com/yhs3434/Algorithms

t = int(input())
for xxx in range(t):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    print(sum(arr))