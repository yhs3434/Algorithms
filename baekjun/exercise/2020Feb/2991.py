# 사나운 개
# https://www.acmicpc.net/problem/2991
# https://github.com/yhs3434

a, b, c, d = map(int, input().split(' '))
p, m, n = map(int, input().split(' '))

p -= 1
m -= 1
n -= 1

p1 = p % (a+b)
p2 = p % (c+d)

m1 = m % (a+b)
m2 = m % (c+d)

n1 = n % (a+b)
n2 = n % (c+d)

ans = [0, 0, 0]
if p1 < a:
    ans[0] += 1
if p2 < c:
    ans[0] += 1
if m1 < a:
    ans[1] += 1
if m2 < c:
    ans[1] += 1
if n1 < a:
    ans[2] += 1
if n2 < c:
    ans[2] += 1

for a in ans:
    print(a)