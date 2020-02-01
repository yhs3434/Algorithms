# 징검다리
# https://www.acmicpc.net/problem/11561
# https://github.com/yhs3434/Algorithms

MAX = 999999

t = int(input())
for _ in range(t):
    n = int(input())

    answer = 0
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        val = (mid + 1) * mid // 2
        if val <= n:
            left = mid + 1
            if mid > answer:
                answer = mid
        else:
            right = mid - 1
    print(answer)