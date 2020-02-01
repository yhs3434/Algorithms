# 병사 배치하기
# https://www.acmicpc.net/problem/18353
# https://github.com/yhs3434/Algorithms

n = int(input())
arr = list(map(int, input().split(' ')))

def getLowerIdx(arr, val):
    left = 0
    right = len(arr) - 1
    idx = 0

    while left <= right:
        mid = (left + right) // 2

        if val < arr[mid]:
            left = mid + 1
            if mid > idx:
                idx = mid
        elif val > arr[mid]:
            right = mid - 1
        else:
            return -1

    if val <= arr[idx]:
        idx += 1
    return idx

lowerCase = []
for i in range(len(arr)):
    val = arr[i]
    if not lowerCase:
        lowerCase.append(val)
    else:
        idx = getLowerIdx(lowerCase, val)
        if idx == -1:
            continue
        if idx >= len(lowerCase):
            lowerCase.append(val)
        else:
            lowerCase[idx] = val
print(n - len(lowerCase))