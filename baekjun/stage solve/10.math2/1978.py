# 소수 찾기
# https://www.acmicpc.net/problem/1978

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

n = int(input())
nums = list(map(int, input().split(' ')))
maxNum = max(nums)
primes = getPrimes(maxNum)
cnt = 0
for num in nums:
    if num in primes:
        cnt += 1
print(cnt)