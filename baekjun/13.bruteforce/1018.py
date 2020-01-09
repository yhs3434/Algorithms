# 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018

chessBoard1 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
chessBoard2 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

def solution(n, m, boards):
    answer = float('inf')

    for i in range(n - 8 + 1):
        for j in range(m - 8 + 1):
            val = isChess(i, j, boards)
            if val < answer:
                answer = val
    return answer

def isChess(r, c, boards):
    cnt1 = 0
    cnt2 = 0
    for i in range(8):
        for j in range(8):
            if boards[r+i][c+j] != chessBoard1[i][j]:
                cnt1 += 1
            if boards[r+i][c+j] != chessBoard2[i][j]:
                cnt2 += 1
    return min(cnt1, cnt2)

n, m = map(int, input().split(' '))
boards = []
for i in range(n):
    boards.append(input())
print(solution(n, m, boards))