# 나무 자르기
# https://www.acmicpc.net/problem/2805

def solution(n, m, trees):
    left = 0
    right = max(trees)
    answer = 0

    while left<=right:
        mid = (left + right) // 2
        val = getRest(mid, trees)
        if val >= m:
            left = mid + 1
            if mid > answer:
                answer = mid
        else:
            right = mid - 1

    return answer

def getRest(h, trees):
    sumVal = 0
    for tree in trees:
        if tree > h:
            sumVal += (tree - h)
    return sumVal

n, m = map(int, input().split(' '))
trees = list(map(int, input().split(' ')))
print(solution(n, m, trees))