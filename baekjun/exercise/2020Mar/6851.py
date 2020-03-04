# Snowflakes
# https://www.acmicpc.net/problem/6851

# 여러분 모두 힘 내세요
# 저도 코로나로 참 힘드네요 ㅎ_ㅎ..ㅠㅠ

import sys
input = lambda:sys.stdin.readline().rstrip()

def isRight(arr1, arr2):
    for i in range(6):
        minIdx1 = i
        minIdx2 = 0
        flag = True
        i = minIdx1
        j = minIdx2
        for _ in range(6):
            if arr1[i] != arr2[j]:
                flag = False
                break
            i = (i+1)%6
            j = (j+1)%6
        if flag:
            return True
    arr2.reverse()
    for i in range(6):
        flag = True
        minIdx1 = i
        minIdx2 = 0
        i = minIdx1
        j = minIdx2
        for _ in range(6):
            if arr1[i] != arr2[j]:
                flag = False
                break
            i = (i+1)%6
            j = (j+1)%6
        if flag:
            return True
    return False

n = int(input())
myhash = {}
flag = False
flakes = []
for i in range(n):
    arr = list(map(int, input().split()))
    flakes.append(arr)
    curset = set()
    if arr[0] in myhash:
        curset |= (myhash[arr[0]])
    for a in arr:
        if a in myhash:
            curset &= myhash[a]
        else:
            curset &= set()
    if len(curset) > 0:
        for idx in curset:
            if isRight(arr, flakes[idx]):
                flag = True
                break
        if flag:
            break
    for a in arr:
        if a in myhash:
            myhash[a].add(i)
        else:
            myhash[a] = set([i])

if flag:
    print('Twin snowflakes found.')
else:
    print('No two snowflakes are alike.')
