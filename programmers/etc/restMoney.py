# 연습문제 - 거스름돈
# https://programmers.co.kr/learn/courses/30/lessons/12907

def solution(n, money):
    answer = 0

    money.sort()

    dp = [[0 for j in range(n+1)] for i in range(2)]
    for i in range(n+1):
        if i%money[0] == 0:
            dp[0][i] = 1

    for i in range(1, len(money)):
        curMoney = money[i]
        ii = i % 2
        for j in range(n+1):
            idx = j
            sumVal = 0
            if ii==0:
                sumVal = dp[ii+1][idx]
                if idx-curMoney>=0:
                    sumVal += dp[ii][idx-curMoney]
            else:
                sumVal = dp[ii-1][idx]
                if idx-curMoney>=0:
                    sumVal += dp[ii][idx-curMoney]
            dp[ii][j] = sumVal
    answer = dp[ii][-1]

    return answer%1000000007

print(solution(5, [1,2,5]))
