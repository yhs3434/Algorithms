# 공유기 설치
# https://www.acmicpc.net/problem/2110
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline

def isPossible(arr, dist, C):
    prev = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] - prev >= dist:
            cnt += 1
            prev = arr[i]
    if cnt >= C:
        return True
    else:
        return False

N, C = map(int, input().split(' '))
arr = []
for _ in range(N):
    arr.append(int(rl().rstrip()))

arr.sort()

left = 1
right = arr[-1] - arr[0]
answer = 0
while left <= right:
    mid = (left + right) // 2

    if isPossible(arr, mid, C):
        if mid > answer:
            answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)