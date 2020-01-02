# 서머코딩 / 윈터코딩 (~2018) - 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def solution(nums):
    answer = 0

    primes = getPrimes()
    combis = list(combinations(nums, 3))
    for combi in combis:
        num = sum(combi)
        if isPrime(num, primes):
            answer += 1
    return answer

def isPrime(num, primes):
    if num in primes:
        return True
    else:
        return False

def getPrimes():
    che = [i for i in range(3, 3001, 2)]
    che = [2] + che
    n = che.pop(0)
    primes = [n]
    while che:
        lChe = len(che)
        for i in range(lChe):
            i = lChe - i - 1
            if che[i] % n == 0:
                del che[i]
        n = che.pop(0)
        primes.append(n)
    return primes


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))