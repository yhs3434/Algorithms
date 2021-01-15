from collections import deque

N = int(input())
A = [0] + list(map(int, input().split()))
P = list(map(int, input().split()))

tree = {}
for i in range(1,N+1):
    tree[i] = set()

for i in range(len(P)):
    j = i+2
    n = P[i]
    tree[n].add(j)

cnt = 0

q = deque()
q.append((1, set()))    # cnode, visited

while q:
    cur = q.popleft()
    cidx = cur[0]
    cvisit = cur[1]

    for nidx in tree[cidx]:
        cval = A[cidx]
        nval = A[nidx]
        if cval >= nval:
            if cval % nval == 0:
                cnt += 1
        else:
            if nval % cval == 0:
                cnt += 1
        for pidx in cvisit:
            pval = A[pidx]
            if pval >= nval:
                if pval % nval == 0:
                    cnt += 1
            else:
                if nval % pval == 0:
                    cnt += 1
        q.append((nidx, cvisit | {cidx}))
print(cnt)