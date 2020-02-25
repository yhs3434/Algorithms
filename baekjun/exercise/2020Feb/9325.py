# 얼마?
# https://www.acmicpc.net/problem/9325
# https://github.com/yhs3434/Algorithms

t = int(input())

for _ in range(t):
    ans = 0
    s = int(input())
    n = int(input())
    ans += s
    for __ in range(n):
        q, p = map(int, input().split(' '))
        ans += (q*p)
    print(ans)