# 단어 뒤집기
# https://www.acmicpc.net/problem/9093
# https://github.com/yhs3434/Algorithms

t = int(input())
for xxx in range(t):
    inp = input().split(' ')
    for strr in inp:
        print(strr[::-1], end=' ')