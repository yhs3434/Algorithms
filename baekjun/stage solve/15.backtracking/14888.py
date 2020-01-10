# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

def myCal(modis):
    for i in range(1, len(modis), 2):
        if modis[i] == 1000000003:
            modis[i+1] = modis[i-1]*modis[i+1]
        elif modis[i] == 1000000004:
            modis[i+1] = getDivide(modis[i-1], modis[i+1])
        elif modis[i] == 1000000001:
            modis[i+1] = modis[i-1] + modis[i+1]
        elif modis[i] == 1000000002:
            modis[i + 1] = modis[i - 1] - modis[i + 1]
    return modis[-1]

def getDivide(a, b):
    return int(a/b)

import queue

n = int(input())
nums = list(map(int, input().split(' ')))
opers = list(map(int, input().split(' ')))

answer = []
q = queue.Queue()
q.put((0, [])) # (연산자 수, 연산자)
while not q.empty():
    cur = q.get()
    cN = cur[0]
    cOpers = cur[1]

    if cN == n-1:
        answer.append(cOpers)
    else:
        for i in range(4):
            if cOpers.count(i) < opers[i]:
                q.put((cN + 1, cOpers + [i]))

modis = [[] for i in range(len(answer))]
for k in range(len(modis)):
    i = 0
    j = 0
    while i < n:
        if i == j:
            modis[k].append(nums[i])
            i += 1
        else:
            modis[k].append(answer[k][j])
            j += 1
    for l in range(1, len(modis[k]), 2):
        modis[k][l] = 1000000001 + modis[k][l]

maxVal = -float('inf')
minVal = float('inf')
for i in range(len(modis)):
    val = myCal(modis[i])
    if val > maxVal:
        maxVal = val
    if val < minVal:
        minVal = val
print(maxVal)
print(minVal)