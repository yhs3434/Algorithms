# 이항 계수 1
# https://www.acmicpc.net/problem/11050

n, k = map(int, input().split(' '))

k = min(k, n-k)
supVal = 1
for i in range(n, n-k, -1):
    supVal *= i
subVal = 1
for i in range(2, k+1):
    subVal *= i
print(supVal//subVal)