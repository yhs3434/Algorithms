# https://www.acmicpc.net/problem/1110

import sys

answer = 0
n = int(sys.stdin.readline().rstrip())
x = n
while True:
    answer += 1
    x = (x//10 + x%10)%10 + x%10*10
    if x == n:
        break
print(answer)