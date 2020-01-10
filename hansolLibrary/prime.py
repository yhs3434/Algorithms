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