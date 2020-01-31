# 암호코드
# https://www.acmicpc.net/problem/2011
# https://github.com/yhs3434/Algorithms

MOD = 1000000

num = '0' + input()
dp = [1] * (len(num))

if int(num[1]) == 0:
    print(0)

else:
    for i in range(2, len(num)):
        val = 0
        if 1<=int(num[i])<=9:
            val += dp[i-1]
        if 10<=int(num[i-1:i+1])<=26:
            val += dp[i-2]
        dp[i] = val%MOD

    print(dp[-1])