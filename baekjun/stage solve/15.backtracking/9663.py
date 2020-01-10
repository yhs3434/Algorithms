# N-Queen
# https://www.acmicpc.net/problem/9663

#import queue

n = int(input())

#q = queue.Queue()
#q.put((0, []))  # (r, 놓은 번호)
st = []
st.append((0, [16 for i in range(n)]))
cnt = 0
while st:
    cur = st.pop()
    r = cur[0]
    cPut = cur[1]

    if r == n:
        cnt += 1
    else:
        for j in range(n):
            if j not in cPut:
                k = 1
                flag = True
                while r-k >= 0:
                    if j-k < 0 and j+k >=n:
                        break
                    if j-k == cPut[r-k] or j+k == cPut[r-k]:
                        flag = False
                        break
                    k+=1
                if flag:
                    cPut[r] = j
                    st.append((r+1, cPut[:]))
                    cPut[r] = 16
print(cnt)