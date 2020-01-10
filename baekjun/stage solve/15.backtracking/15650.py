# N과 M (2)
# https://www.acmicpc.net/problem/15650

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
        si = 0
        if not cNums:
            si = 1
        else:
            si = cNums[-1] + 1
        for i in range(si, m+1):
            if i not in cNums:
                q.put((cNums+[i], cN+1))
for x in arr:
    for y in x:
        print(y, end=' ')
    print('')