# 숫자 카드 2
# https://www.acmicpc.net/problem/10816

import sys
rl = sys.stdin.readline

def solution(arr1, arr2):
    arr1.sort()
    arr1 = [-float('inf')] + arr1 + [float('inf')]

    for x in arr2:
        i, j = bs(arr1, x)
        cnt = j - i
        print(cnt, end=' ')
    return

def bs(arr1, val):
    left = 0
    right = len(arr1) - 1
    idx1 = 0
    while left<=right:
        mid = (left + right) // 2
        if val <= arr1[mid]:
            right = mid - 1
        else:
            left = mid + 1
            if mid > idx1:
                idx1 = mid
    left = 0
    right = len(arr1) - 1
    idx2 = 500001
    while left<=right:
        mid = (left + right) // 2
        if val < arr1[mid]:
            right = mid - 1
            if mid < idx2:
                idx2 = mid
        else:
            left = mid + 1
    return idx1 + 1, idx2

n = int(rl().rstrip())
arr1 = list(map(int, rl().rstrip().split(' ')))
m = int(rl().rstrip())
arr2 = list(map(int, rl().rstrip().split(' ')))
solution(arr1, arr2)