# 욱 제
# https://www.acmicpc.net/problem/17356
# https://github.com/yhs3434

a, b = map(int, input().split(' '))

m = (b-a)/400
answer = 1/(1+10**m)
print(answer)