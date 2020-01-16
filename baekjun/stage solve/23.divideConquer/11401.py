# 이항 계수 3
# https://www.acmicpc.net/problem/11401

_MOD_ = 1000000007
_MAX_SIZE_ = 4000000
n, k = map(int, input().split(' '))
dp = [1] * (_MAX_SIZE_ + 1)

supVal = 1
for i in range(2, n+1):
    supVal = (supVal * i)%_MOD_
    dp[i] = supVal

subVal1 = dp[k]
subVal2 = dp[n-k]

uc = [[0]*4 for i in range(2)]
uc[0][0] = 1
uc[0][1] = 0
uc[0][2] = subVal1
uc[1][0] = 0
uc[1][1] = 1
uc[1][2] = _MOD_
uc[1][3] = uc[0][2] // uc[1][2]
i = 1
while True:
    i += 1
    uc.append([0, 0, 0, 0])
    uc[i][0] = uc[i-2][0] - uc[i-1][0]*uc[i-1][3]
    uc[i][1] = uc[i-2][1] - uc[i-1][1]*uc[i-1][3]
    uc[i][2] = uc[i-2][2] % uc[i-1][2]
    if uc[i][2] == 0:
        break
    uc[i][3] = uc[i-1][2] // uc[i][2]
s = uc[i-1][0]
while s<0:
    s = (s + _MOD_) % _MOD_
s1 = s

uc = [[0]*4 for i in range(2)]
uc[0][0] = 1
uc[0][1] = 0
uc[0][2] = subVal2
uc[1][0] = 0
uc[1][1] = 1
uc[1][2] = _MOD_
uc[1][3] = uc[0][2] // uc[1][2]
i = 1
while True:
    i += 1
    uc.append([0, 0, 0, 0])
    uc[i][0] = uc[i-2][0] - uc[i-1][0]*uc[i-1][3]
    uc[i][1] = uc[i-2][1] - uc[i-1][1]*uc[i-1][3]
    uc[i][2] = uc[i-2][2] % uc[i-1][2]
    if uc[i][2] == 0:
        break
    uc[i][3] = uc[i-1][2] // uc[i][2]
s = uc[i-1][0]
while s<0:
    s = (s + _MOD_) % _MOD_
s2 = s

print((supVal*s1 * s2)%_MOD_)