# 피보나치 수 3
# https://www.acmicpc.net/problem/2749

_MOD_ = 1000000
arrr = [0] * 1500001
def getCycle(m):
    dp = [0, 1, 0]
    cnt = 1
    i = 1
    val = -1
    while val!=0:
        cnt += 1
        i = (i+1)%3
        dp[i] = (dp[i-1] + dp[i-2]) % _MOD_
        arrr[cnt] = dp[i]
        if dp[i] == 0 and dp[i-1] == 1:
            break
    return cnt


n = int(input())

cycle = getCycle(n)

n %= cycle
if n==1:
    print(1)
else:
    print(arrr[n])