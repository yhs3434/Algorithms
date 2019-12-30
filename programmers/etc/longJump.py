# 멀리 뛰기
# https://programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    answer = 0

    if n==1:
        return 1
    if n==2:
        return 2

    dp = [0 for i in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[-1]

    return answer%1234567

import queue

def solution2(n):
    answer = 0

    q = queue.Queue()
    q.put(n)
    cases = []
    while not q.empty():
        cur = q.get()
        curN = cur

        for i in range(1, 3):
            newN = curN - i
            if newN <= 0:
                if newN == 0:
                    answer += 1
            else:
                q.put(newN)

    return answer


print(solution(100))
print(solution(100))
print(solution(4))
print(solution(3))