# 스타트와 링크
# https://www.acmicpc.net/problem/14889

def solution(n, board):
    answer = float('inf')

    st = []
    st.append((0, []))  # (팀원 수, 팀원)
    while st:
        cur = st.pop()
        cN = cur[0]
        cTeam = cur[1]

        if cN == (n//2):
            ab1 = 0
            ab2 = 0
            for i in cTeam:
                for j in cTeam:
                    ab1 += board[i][j]
            for i in range(n):
                if i not in cTeam:
                    for j in range(n):
                        if j not in cTeam:
                            ab2 += board[i][j]
            val = abs(ab1-ab2)
            if val < answer:
                answer = val
        else:
            si = 0
            if cTeam:
                si = cTeam[-1] + 1
            for i in range(si, n):
                if i not in cTeam:
                    st.append((cN+1, cTeam+[i]))

    return answer

n = int(input())
board = []
for xxx in range(n):
    board.append(list(map(int, input().split(' '))))
print(solution(n, board))