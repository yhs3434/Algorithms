# 주사위 굴리기
# https://www.acmicpc.net/problem/14499
# https://github.com/yhs3434/Algorithms

import numpy as np

nrcs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

dice = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

n, m, x1, y1, k = map(int, input().split(' '))
board = []
for xxx in range(n):
    board.append(list(map(int, input().split(' '))))
orders = list(map(int, input().split(' ')))

print(np.array(board))
print(orders)

