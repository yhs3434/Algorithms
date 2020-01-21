# 비밀 이메일
# https://www.acmicpc.net/problem/2999
# https://github.com/yhs3434/Algorithms

inp = input()
n = len(inp)
r, c = 0, 0
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        r, c = i, n//i

answer = ''
for i in range(0, r):
    for j in range(0, n, r):
        answer += inp[j+i]
print(answer)