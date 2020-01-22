# 토너먼트
# https://www.acmicpc.net/problem/1057
# https://github.com/yhs3434/Algorithms

n, a, b = map(int, input().split(" "))

a -= 1
b -= 1

cnt = 1
delim = 2
while a//delim!=b//delim:
    delim*=2
    cnt += 1
print(cnt)