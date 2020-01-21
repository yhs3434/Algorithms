# 멀티탭 스케줄링
# https://www.acmicpc.net/problem/1700
# https://github.com/yhs3434

n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

pluged = [arr[0]]
st = []
st.append((1, 0, pluged[:]))    # (idx, cnt, pluged)
answer = float('inf')
while st:
    cur = st.pop()
    cIdx = cur[0]
    cCnt = cur[1]
    cPluged = cur[2]

    if cIdx == k:
        if cCnt < answer:
            answer = cCnt
        continue

    if cCnt >= answer:
        continue

    if len(cPluged) < n:
        if arr[cIdx] not in cPluged:
            st.append((cIdx+1, cCnt, cPluged + [arr[cIdx]]))
        else:
            st.append((cIdx+1, cCnt, cPluged))
    else:
        if arr[cIdx] in cPluged:
            st.append((cIdx+1, cCnt, cPluged))
        else:
            for p in cPluged:
                tempPluged = cPluged[:]
                tempPluged.remove(p)
                st.append((cIdx+1, cCnt+1, tempPluged + [arr[cIdx]]))
print(answer)