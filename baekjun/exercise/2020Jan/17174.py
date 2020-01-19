# 전체 계산 횟수
# https://www.acmicpc.net/problem/17174
# https://github.com/yhs3434

n, m = map(int, input().split(' '))
answer = 0

while n > 0:
    answer += n
    n //= m
print(answer)