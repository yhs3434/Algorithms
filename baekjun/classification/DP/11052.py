# 카드 구매하기
# https://www.acmicpc.net/problem/11052
# https://github.com/yhs3434

n = int(input())
cards = list(map(int, input().split(' ')))
dp = [0] * (n+1)
cards = [0] + cards

for i in range(1, n+1):
    temp = 0
    for j in range(1, i):
        temp = max(dp[j] + dp[i-j], temp)
    dp[i] = max(cards[i], temp)
print(dp[-1])