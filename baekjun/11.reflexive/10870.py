# 피보나치 수 5
# https://www.acmicpc.net/problem/10870

def pivo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return pivo(n-1)+pivo(n-2)
n = int(input())
print(pivo(n))