from heapq import heappush, heappop, heapify
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    newArr = []
    flag = True
    while arr:
        cur = arr.pop()
        if flag:
            newArr = newArr + [cur]
            flag = False
        else:
            newArr = [cur] + newArr
            flag = True
    maxVal = abs(newArr[0] - newArr[-1])
    for i in range(len(newArr) - 1):
        maxVal = max(maxVal, abs(newArr[i] - newArr[i+1]))
    print(maxVal)