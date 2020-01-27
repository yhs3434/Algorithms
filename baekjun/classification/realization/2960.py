# 에라토스테네스의 체
# https://www.acmicpc.net/problem/2960
# https://github.com/yhs3434/Algorithms

n, k = map(int, input().split(' '))

primes = []
che = [i for i in range(2, n+1)]
cnt = 0
answer = 0

while cnt < k:
    cur = che[0]
    x = 1
    val = cur * x
    while val <= n:
        val = cur * x
        if val in che:
            che.remove(val)
            cnt += 1
            if cnt == k:
                answer = val
        x += 1
print(answer)