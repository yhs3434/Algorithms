from collections import deque

A, B = map(int, input().split())
cnt = 0

q = deque()
q.append('')

while q:
    cur = q.popleft()
    n1 = cur + '4'
    n2 = cur + '7'
    intn1 = int(n1)
    intn2 = int(n2)

    if len(n2) <= len(str(B)) + 1:
        q.append(n1)
        if A <= intn1 <= B:
            cnt += 1
        q.append(n2)
        if A <= intn2 <= B:
            cnt += 1
print(cnt)