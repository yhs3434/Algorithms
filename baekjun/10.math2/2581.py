# 소수
# https://www.acmicpc.net/problem/2581

def getPrimes(n):
    che = [i for i in range(2, n+1)]
    primes = []
    while che:
        cur = che.pop(0)
        primes.append(cur)
        for i in range(len(che)-1, -1, -1):
            if che[i] % cur==0:
                del che[i]
    return primes

m = int(input())
n = int(input())
primes = getPrimes(n)
nPrimes = []
for i in range(m, n+1):
    if i in primes:
        nPrimes.append(i)
if len(nPrimes) > 0:
    print(sum(nPrimes))
    print(min(nPrimes))
else:
    print(-1)