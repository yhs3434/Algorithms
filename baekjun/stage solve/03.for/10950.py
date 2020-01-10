def solution(A, B):
    answer = A + B
    return answer

T = int(input())
for xxx in range(T):
    A, B = map(int, input().split(' '))
    print(solution(A, B))
