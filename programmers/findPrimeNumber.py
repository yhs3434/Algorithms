# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 1

    numbers = set([i for i in range(3,n+1, 2)])
    primes = [2]
    for i in range(3, n+1, 2):
        if(i in numbers):
            primes.append(i)
            removeSet = set([j for j in range(i, n+1, i)])
            numbers -= removeSet
            answer += 1
    return answer

print(solution(10))

