# 다항식과 쿼리
# https://www.acmicpc.net/problem/14882
# https://github.com/yhs3434

def solution(N, A, x):
    dp = [0] * (N+1)
    dp[0] = 1
    cycle = N+1
    for i in range(1, N+1):
        dp[i] = (dp[i-1] * x) % 786433
        if dp[i] == 1:
            cycle = i
            break
    sumVal = 0
    for i in range(N+1):
        sumVal += A[i]*dp[i%cycle]
    return sumVal

N = int(input())
Ai = list(map(int, input().split(' ')))
K = int(input())
Xi = list(map(int, input().split(' ')))

M = max(Xi)
dp = [0] * (M+1)

for x in Xi:
    print(solution(N, Ai, x))