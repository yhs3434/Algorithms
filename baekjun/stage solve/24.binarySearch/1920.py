# 수 찾기
# https://www.acmicpc.net/problem/1920

def solution(arr1, arr2):
    arr1.sort()

    for x in arr2:
        if findBinary(arr1, x):
            print(1)
        else:
            print(0)

    return

def findBinary(arr1, x):
    left = 0
    right = len(arr1) - 1
    while left <= right:
        mid = (left + right)//2
        if arr1[mid] == x:
            return True
        elif x < arr1[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False


n = int(input())
arr1 = list(map(int, input().split(' ')))
m = int(input())
arr2 = list(map(int, input().split(' ')))
solution(arr1, arr2)