# 4936. 섬의 개수
# https://www.acmicpc.net/problem/4963

import queue

def solution(board):
    answer = 0
    w = len(board[0])
    h = len(board)

    islands = []

    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                islands.append((i, j))

    q = queue.Queue()
    while islands:
        answer += 1
        q.put(islands.pop(0))
        while not q.empty():
            cur = q.get()
            r = cur[0]
            c = cur[1]
            temp = (r-1 , c)
            if temp in islands:
                q.put(temp)
                islands.remove(temp)
            temp = (r-1, c+1)
            if temp in islands:
                q.put(temp)
                islands.remove(temp)
            temp = (r, c+1)
            if temp in islands:
                q.put(temp)
                islands.remove(temp)
            temp = (r+1, c+1)
            if temp in islands:
                q.put(temp)
                islands.remove(temp)
            temp = (r+1, c)
            if temp in islands:
                q.put(temp)
                islands.remove(temp)
            temp = (r+1, c-1)
            if temp in islands:
                q.put(temp)
                islands.remove(temp)
            temp = (r, c-1)
            if temp in islands:
                q.put(temp)
                islands.remove(temp)
            temp = (r-1, c-1)
            if temp in islands:
                q.put(temp)
                islands.remove(temp)
    return answer


while True:
    w, h = map(int, input().split(' '))
    if w==0 and h==0:
        break

    board = []
    for qq in range(h):
        board.append(list(map(int, input().split(' '))))

    print(solution(board))