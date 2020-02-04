# 스위치 켜고 끄기
# https://www.acmicpc.net/problem/1244
# https://github.com/yhs3434/Algorithms

def convertButton(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0

def convertSwitch(arr, a, b):
    if a == 1:
        for i in range(b-1, len(arr), b):
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0
    elif a == 2:
        b = b-1
        i = 0
        while 0 <= b-i and b+i < len(arr):
            if arr[b-i] == arr[b+i]:
                if b-i == b+i:
                    arr[b-i] = convertButton(arr[b-i])
                else:
                    arr[b-i] = convertButton(arr[b-i])
                    arr[b+i] = convertButton(arr[b+i])
                i += 1
            else:
                break

N = int(input())
arr = list(map(int, input().split(' ')))
M = int(input())
for _ in range(M):
    a, b = map(int, input().split(' '))
    convertSwitch(arr, a, b)
for i in range(len(arr)):
    print(arr[i], end = ' ')
    if (i+1) % 20 == 0:
        print('')