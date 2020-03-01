# 큰 수 구성하기
# https://www.acmicpc.net/problem/18511

# 이 글 보시는 분들 모두 힘내시고, 코로나 잘 이겨내세요

N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

st = []
st.append(('', 0))
avails = []
while st:
    cur = st.pop()
    cStr = cur[0]
    cLen = cur[1]

    if cLen == len(str(N)):
        avails.append(int(cStr))
    else:
        for a in arr:
            st.append((cStr + str(a), cLen + 1))
        if cLen == 0:
            st.append((cStr + str(0), cLen + 1))
avails.sort(reverse=True)
for a in avails:
    if a <= N:
        print(a)
        break