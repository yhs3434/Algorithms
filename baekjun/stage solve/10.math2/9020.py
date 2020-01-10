# 골드바흐의 추측
# https://www.acmicpc.net/problem/9020

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

t = int(input())

for xxx in range(t):
    num = int(input())
    primes = getPrimes(1, num)
    answer = [0, 0]
    for i in range(num//2, num):
        if i in primes:
            if num-i in primes:
                answer = [num-i, i]
                break
    answer.sort()
    print(answer[0], answer[1])