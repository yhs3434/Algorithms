# 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729

def solution(K):
    answer = 0
    moves = []
    hanoi(K, 1, 2, 3, moves)
    print(len(moves))
    for move in moves:
        print(move[0], move[1])
    return answer

def moveTo(f, t, moves):
    moves.append((f, t))

def hanoi(n, f, b, t, moves):
    if n == 1:
        moveTo(f, t, moves)
        return
    hanoi(n-1, f, t, b, moves)
    moveTo(f, t, moves)
    hanoi(n-1, b, f, t, moves)


K = int(input())
solution(K)