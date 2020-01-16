# 피사노 주기
# https://www.acmicpc.net/problem/9471

def solution(m):
    dp = [0, 1, 0]
    cnt = 1
    i = 1
    val = -1
    while val!=0:
        cnt += 1
        i = (i+1)%3
        dp[i] = (dp[i-1] + dp[i-2]) % m
        if dp[i] == 0 and dp[i-1] == 1:
            break
    return cnt

t = int(input())
for xxx in range(t):
    n, m = map(int, input().split(' '))
    print(n,solution(m))
