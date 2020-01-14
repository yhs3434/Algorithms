# 백대열
# https://www.acmicpc.net/problem/14490

n, m = map(int, input().split(':'))
a, b = n, m
while n!=m:
    if n>m:
        n = abs(n-m)
    else:
        m = abs(n-m)
print(str(a//n)+':'+str(b//n))