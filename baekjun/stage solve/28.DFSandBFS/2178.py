# 미로 탐색
# https://www.acmicpc.net/problem/2178
# https://github.com/yhs3434/Algorithms

n, m = map(int, input().split(' '))
board = []
for i in range(n):
    board.append(input())
dp = [[0] * m for i in range(n)]
dp[0][0] = 1
st = []
st.append((0, 0, 1))    # (r, c, cnt)
answer = float('inf')

while st:
    cur = st.pop()
    r = cur[0]
    c = cur[1]
    cCnt = cur[2]

    if cCnt > answer:
        continue
    if r == n-1 and c == m-1:
        if cCnt < answer:
            answer = cCnt

    if r-1 >= 0 and board[r-1][c] == '1':
        if dp[r-1][c] == 0:
            dp[r-1][c] = cCnt + 1
            st.append((r-1, c, cCnt + 1))
        elif dp[r-1][c] > cCnt+1:
            dp[r-1][c] = cCnt + 1
            st.append((r-1, c, cCnt + 1))
    if c+1 < m and board[r][c+1] == '1':
        if dp[r][c+1] == 0:
            dp[r][c+1] = cCnt + 1
            st.append((r, c+1, cCnt + 1))
        elif dp[r][c+1] > cCnt+1:
            dp[r][c+1] = cCnt + 1
            st.append((r, c+1, cCnt + 1))
    if r+1 < n and board[r+1][c] == '1':
        if dp[r+1][c] == 0:
            dp[r+1][c] = cCnt + 1
            st.append((r+1, c, cCnt + 1))
        elif dp[r+1][c] > cCnt+1:
            dp[r+1][c] = cCnt + 1
            st.append((r+1, c, cCnt + 1))
    if c-1 >= 0 and board[r][c-1] == '1':
        if dp[r][c-1] == 0:
            dp[r][c-1] = cCnt + 1
            st.append((r, c-1, cCnt + 1))
        elif dp[r][c-1] > cCnt+1:
            dp[r][c-1] = cCnt + 1
            st.append((r, c-1, cCnt + 1))
print(answer)