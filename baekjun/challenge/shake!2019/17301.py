# NC 문자열
# https://www.acmicpc.net/problem/17301

import sys
rl = sys.stdin.readline

_MOD_ = 1000000007

ncs2 = [0, 0, 0, 0]

#ncs = {
#    'N' : 0,
#    'C' : 0,
#    'NC' : 0,
#    'CN' : 0
#}

def getInverse(a, p):
    uc = [[1,0,a,0], [0,1,p,a//p]]
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
        s = (s + p) % p
    return s

def getPermutation(n, k):
    if n == 0:
        return 1
    if n == 1:
        return 1
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1]*i) % _MOD_
    supVal = dp[n]
    subVal = getInverse(dp[n-k], _MOD_)

    return (supVal*subVal) % _MOD_

def getVol(n):
    vol = 0
    for i in range(n + 1):
        vol += getPermutation(n, i)
    return vol

n = int(rl().rstrip())
for xxx in range(n):
    strr = rl().rstrip()
    if strr.count('N') == 0:
        #ncs['C'] += 1
        ncs2[1] += 1
    elif strr.count('C') == 0:
        #ncs['N'] += 1
        ncs2[0] += 1
    else:
        nflag = False
        ncflag = False
        for c in strr:
            if c == 'N':
                nflag = True
            elif c == 'C':
                if nflag:
                    #ncs['NC'] += 1
                    ncs2[2] += 1
                    ncflag = True
                    break
        if not ncflag:
            #ncs['CN'] += 1
            ncs2[3] += 1

volDp = [0] * (n+1)
volDp[0] = 1
for i in range(1, n+1):
    volDp[i] = (volDp[i-1] * i + 1)%_MOD_

totalVol = volDp[n]
#cVol = volDp[ncs['C']]
cVol = volDp[ncs2[1]]
#cnVol = ncs['CN'] + 1
cnVol = ncs2[3] + 1
#nVol = volDp[ncs['N']]
nVol = volDp[ncs2[0]]
answer = (totalVol - (cVol*cnVol*nVol))%_MOD_
print(answer)