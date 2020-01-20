# 이친수
# https://www.acmicpc.net/problem/2193
# https://github.com/yhs3434

n = int(input())
fiv = [0] * (n+1)
fiv[1] = 1
for i in range(2, n+1):
    fiv[i] = fiv[i-1] + fiv[i-2]
print(fiv[n])