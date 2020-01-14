# 조합 0의 개수
# https://www.acmicpc.net/problem/2004

def solution(n, m):
    cnt1 = 0
    cnt11 = 0
    cnt2 = 0
    cnt22 = 0
    cnt3 = 0
    cnt33 = 0

    i = 1
    while 5**i <= n:
        cnt1 += (n//(5**i))
        i += 1
    i = 1
    while 5 ** i <= m:
        cnt2 += (m // (5 ** i))
        i += 1
    i = 1
    while 5 ** i <= (n-m):
        cnt3 += ((n-m) // (5 ** i))
        i += 1

    i = 1
    while 2 ** i <= n:
        cnt11 += (n // (2 ** i))
        i += 1
    i = 1
    while 2 ** i <= m:
        cnt22 += (m // (2 ** i))
        i += 1
    i = 1
    while 2 ** i <= (n - m):
        cnt33 += ((n - m) // (2 ** i))
        i += 1

    n2 = cnt11 - (cnt22+cnt33)
    n5 = cnt1 - (cnt2+cnt3)
    return min(n2, n5)

n, m = map(int, input().split(' '))
print(solution(n, m))