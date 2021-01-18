N, M, K = map(int, input().split())

answer = 0

for i in range(K+1):
    a = N - K + i
    b = M - i
    if a < 0 or b < 0:
        continue
    temp = min(a//2, b)
    answer = max(answer, temp)
print(answer)