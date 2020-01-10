# 베르트랑 공준
# https://www.acmicpc.net/problem/4948

def getPrimes(m, n):
    che = [False, False] + [True] * (n-1)
    primes = []
    for i in range(2, n+1):
        if che[i]:
            if i >= m:
                primes.append(i)
            for j in range(2*i, n+1, i):
                che[j] = False
    return primes

while True:
    n = int(input())
    if n == 0:
        break
    primes = getPrimes(n+1, 2*n)
    print(len(primes))