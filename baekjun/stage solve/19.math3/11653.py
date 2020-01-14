# 소인수분해
# https://www.acmicpc.net/problem/11653

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

def solution(n):
    if n==1:
        return 1
    primes = getPrimes(1, n)
    primes.sort(reverse=True)
    cp = 999999
    answer = []
    while n>1:
        while primes and n%cp != 0:
            cp = primes.pop()
        answer.append(cp)
        n //= cp
    return answer

n = int(input())
answer = solution(n)
answer.sort()
for a in answer:
    print(a)