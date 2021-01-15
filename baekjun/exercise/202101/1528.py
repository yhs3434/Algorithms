from collections import deque

answer = [-1]
N = int(input())

nums = []
track = [False] * (N+1)

q = deque()

q.append('')
while q:
    cur = q.popleft()
    n1 = cur + '4'
    n2 = cur + '7'
    intn1 = int(n1)
    intn2 = int(n2)
    if intn1 <= N:
        nums.append(intn1)
        q.append(n1)
    if intn2 <= N:
        nums.append(intn2)
        q.append(n2)

q.append((0, []))
while q:
    cur = q.popleft()
    cn = cur[0]
    csolution = cur[1]

    if cn == N:
        answer = csolution

    for num in nums:
        nn = cn + num
        if nn <= N and not track[nn]:
            track[nn] = True
            q.append((nn, csolution + [num]))

for a in answer:
    print(a, end=' ')