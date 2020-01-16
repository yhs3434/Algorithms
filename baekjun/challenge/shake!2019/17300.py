# 패턴
# https://www.acmicpc.net/problem/17300

gapHash = {}
gapHash[(1, 3)] = 2
gapHash[(3, 1)] = 2
gapHash[(4, 6)] = 5
gapHash[(6, 4)] = 5
gapHash[(7, 9)] = 8
gapHash[(9, 7)] = 8
gapHash[(1, 7)] = 4
gapHash[(7, 1)] = 4
gapHash[(2, 8)] = 5
gapHash[(8, 2)] = 5
gapHash[(3, 9)] = 6
gapHash[(9, 3)] = 6
gapHash[(1, 9)] = 5
gapHash[(9, 1)] = 5
gapHash[(3, 7)] = 5
gapHash[(7, 3)] = 5

def solution(l, A):
    board = [False for i in range(10)]
    for i in range(len(A)-1):
        cur = A[i]
        nex = A[i+1]
        board[cur] = True
        if (cur, nex) in gapHash:
            if not board[gapHash[(cur, nex)]]:
                return 'NO'
        else:
            if board[nex]:
                return 'NO'
    return 'YES'

l = int(input())
A = list(map(int, input().split(' ')))
print(solution(l, A))