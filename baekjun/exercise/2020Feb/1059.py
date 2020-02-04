# 수2
# https://www.acmicpc.net/problem/1059
# https://github.com/yhs3434/Algorithms

L = int(input())
lucky = list(map(int, input().split(' ')))
lucky.sort()
N = int(input())

if N in lucky:
    print(0)
else:
    left = 0
    right = 0
    idx = 0
    for i in range(len(lucky)):
        if N < lucky[i]:
            right = lucky[i]
            break
        else:
            left = lucky[i]

    left += 1
    right -= 1

    arr = []
    for i in range(left, right+1):
        arr.append(i)
    print(len(arr)-1 + (N-left)*(right-N))