N = int(input())

answer = 1

for i in range(N-3, N+1):
    answer *= i
print(answer//24)