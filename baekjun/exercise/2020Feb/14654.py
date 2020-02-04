# 스테판 쿼리
# https://www.acmicpc.net/problem/14654
# https://github.com/yhs3434/Algorithms

def whoWin(x, y):
    if x==y:
        return 2
    if x==1 and y==2:
        return 1
    if x==2 and y==3:
        return 1
    if x==3 and y==1:
        return 1
    return 0

def switch(n):
    if n==0:
        return 1
    else:
        return 0

n = int(input())
arr1 = list(map(int, input().split(' ')))
arr2 = list(map(int, input().split(' ')))

maxCnt = 0
cnt = [0, 0]
bef = 0
for i in range(n):
    ww = whoWin(arr1[i], arr2[i])
    if ww == 2:
        if bef == 0:
            ww = 1
        else:
            ww = 0
        cnt[ww] += 1
        if cnt[ww] > maxCnt:
            maxCnt = cnt[ww]
        if cnt[ww] == 1:
            cnt[switch(ww)] = 0
        bef = ww
    else:
        cnt[ww] += 1
        if cnt[ww] > maxCnt:
            maxCnt = cnt[ww]
        if cnt[ww] == 1:
            cnt[switch(ww)] = 0
        bef = ww
print(maxCnt)