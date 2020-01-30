# 이상한 술집
# https://www.acmicpc.net/problem/13702
# https://github.com/yhs3434/Algorithms

import sys
rl = sys.stdin.readline

n, k = map(int, input().split(' '))
arr = []
for _ in range(n):
    arr.append(int(rl().rstrip()))

left = 1
right = max(arr)
answer = 0

while left <= right:
    mid = (left + right) // 2

    val = 0
    for i in range(n):
        val += (arr[i]//mid)

    if val >= k:
        left = mid + 1
        if mid > answer:
            answer = mid
    else:
        right = mid - 1
print(answer)