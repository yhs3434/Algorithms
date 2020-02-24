# 숫자 정사각형
# https://www.acmicpc.net/problem/1051
# https://github.com/yhs3434/Algorithms

N, M = map(int, input().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int, list(input()))))

lenn = max(N, M) + 1

flag = False
while not flag and lenn > 0:
    lenn -= 1
    for i in range(N-lenn+1):
        for j in range(M-lenn+1):
            if board[i][j] == board[i+lenn-1][j] == board[i][j+lenn-1] == board[i+lenn-1][j+lenn-1]:
                flag = True
                break
print(lenn**2)