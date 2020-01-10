# N과 M (1)
# https://www.acmicpc.net/problem/15649

import queue

m, n = map(int, input().split(' '))
arr = []
q = queue.Queue()

q.put(([], 0))
while not q.empty():
    cur = q.get()
    cNums = cur[0]
    cN = cur[1]

    if cN == n:
        arr.append(cNums)
    else:
        for i in range(1, m+1):
            if i not in cNums:
                q.put((cNums+[i], cN+1))
for x in arr:
    for y in x:
        print(y, end=' ')
    print('')