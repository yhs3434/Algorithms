# 동전 0
# https://www.acmicpc.net/problem/11047

def solution(coins, K):
    answer = 0

    coins.sort()
    while coins and K>0:
        coin = coins.pop()
        answer += K//coin
        K %= coin

    return answer

N, K = map(int, input().split(' '))
coins = []
for xxx in range(N):
    coins.append(int(input()))
print(solution(coins, K))