n, m = map(int, input().split())

m = min(m, abs(n-m))

sup = 1
sub = 1

cnt = m
while cnt > 0:
    cnt -= 1
    sup *= n
    sub *= m
    n -= 1
    m -= 1
print(sup//sub)