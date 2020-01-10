# 수 정렬하기
# https://www.acmicpc.net/problem/2750

import sys

sys.setrecursionlimit(1000000)

def solution(nums):
    quickSort(nums, 0, len(nums)-1)
    return nums

def quickSort(arr, left, right):
    if left>=right:
        return
    pivot = arr[right]
    i = left
    j = left
    while j<right:
        if arr[j] < pivot:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i+=1
            j+=1
        else:
            j+=1
    temp = arr[i]
    arr[i] = pivot
    arr[right] = temp
    quickSort(arr, left, i-1)
    quickSort(arr, i+1, right)

n = int(input())
arrr = []
for xxx in range(n):
    arrr.append(int(input()))
nums = solution(arrr)
for n in nums:
    print(n)