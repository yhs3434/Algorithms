# 거의 소수
# https://www.acmicpc.net/problem/1456

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

a, b = map(int, input().split(' '))

aa, bb = a**0.5, b**0.5
if aa == int(aa):
    aa = int(aa)
else:
    aa = int(aa) + 1
bb = int(bb)+1

primes = getPrimes(1, bb)
answer = set()
for prime in primes:
    pp = prime*prime
    while pp <= b:
        if pp >= a:
            answer.add(pp)
        pp *= prime
print(len(answer))