from collections import deque

N = int(input())

answer = []
st = []
st.append('2')
st.append('3')
st.append('5')
st.append('7')

while st:
    cur = st.pop()

    if len(cur) == N:
        answer.append(int(cur))
        continue

    nns = [cur+'1', cur+'3', cur+'7', cur+'9']
    for nn in nns:
        nnint = int(nn)
        flag = True
        for i in range(3, int(nnint ** (1/2)) + 1, 2):
            if nnint % i == 0:
                flag = False
                break
        if flag:
            st.append(nn)
answer.sort()
for ans in answer:
    print(ans)