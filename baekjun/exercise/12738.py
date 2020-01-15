# 가장 긴 증가하는 부분 수열 3
# https://www.acmicpc.net/problem/12738

def solution(n, arr):
    lowerCase = []
    for i in range(len(arr)):
        val = arr[i]
        lowerIdx = getLowerIdx(lowerCase, val)
        if lowerIdx == len(lowerCase):
            lowerCase.append(val)
        else:
            lowerCase[lowerIdx] = val
    return len(lowerCase)

def getLowerIdx(lowerCase, val):
    if lowerCase == []:
        return 0
    maxIdx = -1
    left = 0
    right = len(lowerCase) - 1
    if val > lowerCase[-1]:
        maxIdx = right
    elif val >= lowerCase[0]:
        while left <= right:
            mid = (left + right) // 2
            if val > lowerCase[mid]:
                left = mid + 1
                if mid > maxIdx:
                    maxIdx = mid
            elif val < lowerCase[mid]:
                right = mid - 1
            else:
                maxIdx = mid - 1
                break
    return maxIdx + 1

n = int(input())
arr = list(map(int, input().split(' ')))
print(solution(n, arr))