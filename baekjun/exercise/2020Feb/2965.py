# 캥거루 세마리
# https://www.acmicpc.net/problem/2965
# https://github.com/yhs3434/Algorithms

a, b, c = map(int, input().split(' '))
maxVal = max(b-a, c-b)
print(maxVal-1)