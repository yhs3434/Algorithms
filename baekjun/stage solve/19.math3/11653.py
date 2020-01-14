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
    answer = []
    if n==1:
        return []
    i = 2
    while i <= n:
        if n % i == 0:
            answer.append(i)
            n //= i
        else:
            i += 1
    return answer

n = int(input())
answer = solution(n)
answer.sort()
if answer:
    for a in answer:
        print(a)