N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

answer = float('inf')
st = []
for i in range(N):
    st.append((i, {i}, 0, i))   # idx, visited, sum, startidx
while st:
    cur = st.pop()
    cidx = cur[0]
    cvisit = cur[1]
    cprice = cur[2]
    startidx = cur[3]

    if len(cvisit) == N:
        if matrix[cidx][startidx] != 0:
            answer = min(answer, cprice + matrix[cidx][startidx])
    else:
        if cprice <= answer:
            for nidx in range(N):
                if nidx not in cvisit and matrix[cidx][nidx] != 0:
                    st.append((nidx, cvisit|{nidx}, cprice+matrix[cidx][nidx], startidx))

print(answer)