# 진법 변환
# https://www.acmicpc.net/problem/2745
# https://github.com/yhs3434/Algorithms

def bToTen(c):
    if '0' <= c <= '9':
        return int(c)
    else:
        return ord(c) - ord('A') + 10

n, b = input().split(' ')
b = int(b)

cnt = len(n) - 1
answer = 0
for c in n:
    answer += (bToTen(c)*(b**cnt))
    cnt -= 1
print(answer)