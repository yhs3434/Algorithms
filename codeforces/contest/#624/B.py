from collections import deque
import sys
rl = sys.stdin.readline
t = int(input())

def isRight(arr):
    before = -float('inf')
    for a in arr:
        if a < before:
            return False
        before = a
    return True

for _ in range(t):
    n, m = map(int, rl().rstrip().split(' '))
    a = list(map(int, rl().rstrip().split(' ')))
    p = list(map(int, rl().rstrip().split(' ')))
    for i in range(len(p)):
        p[i] -= 1

    visited = {}
    q = deque()
    q.append(a)
    flag = False
    while q:
        cur = q.popleft()
        if isRight(cur):
            flag = True
            break
        for pp in p:
            newCur = cur[:]
            temp = newCur[pp]
            newCur[pp] = newCur[pp+1]
            newCur[pp+1] = temp
            try:
                if visited[str(newCur)] == False:
                    visited[str(newCur)] = True
                    q.append(newCur)
            except:
                visited[str(newCur)] = True
                q.append(newCur)
    if flag:
        print('YES')
    else:
        print('NO')