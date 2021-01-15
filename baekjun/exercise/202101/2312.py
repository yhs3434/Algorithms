T = int(input())

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

for _ in range(T):
    N = int(input())
    primes = getPrimes(2, N)
    for prime in primes:
        flag = True
        cnt = 0
        while flag:
            if N % prime == 0:
                cnt += 1
                N //= prime
            else:
                flag = False
        if cnt > 0:
            print(prime, cnt)