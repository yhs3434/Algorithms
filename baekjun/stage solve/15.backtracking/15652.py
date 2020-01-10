# N과 M (4)
# https://www.acmicpc.net/problem/15652

import queue

m, n = map(int, input().split(' '))
arr = []
#q = queue.Queue()
#q.put(([], 0))
st = []
st.append(([], 0))
while st:
    cur = st.pop()
    cNums = cur[0]
    cN = cur[1]

    if cN == n:
        arr.append(cNums)
    else:
        si = 0
        if not cNums:
            si = 1
        else:
            si = cNums[-1]
        for i in range(si, m+1):
            st.append((cNums+[i], cN+1))
arr.sort()
for x in arr:
    for y in x:
        print(y, end=' ')
    print('')