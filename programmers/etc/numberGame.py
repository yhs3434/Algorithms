# 서머코딩 / 윈터코딩 (~2018)
# https://programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    isWin(A,B,3)

    left = 0
    right = len(A)
    while left <= right:
        mid = (left + right) // 2

        if isWin(A, B, mid):
            left = mid + 1
            if mid > answer:
                answer = mid
        else:
            right = mid - 1

    return answer

def isWin(A, B, n):
    a = A[:n]
    b = B[-n:]
    while a:
        if a.pop() >= b.pop():
            return False
    return True

print(solution([5,1,3,7], [2,2,6,8]))