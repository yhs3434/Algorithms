# 가장 큰 정사각형 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    answer = 0

    map = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if(map[i][j] != 0):
                map[i][j] = min(map[i-1][j-1], map[i-1][j], map[i][j-1]) + 1

    maxes = [max(map[i]) for i in range(len(map))]
    answer = max(maxes)**2
    return answer

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[1,0],[0,0]]))