# 16진수
# https://www.acmicpc.net/problem/1550

def sixteenToTen(n):
    if n >= '0' and n<='9':
        return int(n)
    elif n == 'A':
        return 10
    elif n == 'B':
        return 11
    elif n == 'C':
        return 12
    elif n == 'D':
        return 13
    elif n == 'E':
        return 14
    elif n == 'F':
        return 15

n = input()

delim = 0
answer = 0
for i in range(len(n)-1, -1, -1):
    answer += sixteenToTen(n[i]) * (16**delim)
    delim += 1
print(answer)