# 과일 서리
# https://www.acmicpc.net/problem/17213

def solution(N, M):
    answer = 0

    amount = M - N
    if(N==1):
        return 1
    stack = [(i, 1) for i in range(amount+1)]

    while stack:
        cur = stack.pop()
        curIdx = cur[1]
        curAmount = cur[0]
        if(curIdx == N-2):
            answer += (amount-curAmount+1)
        else:
            for i in range(amount - curAmount + 1):
                stack.append((cur[0]+i, cur[1]+1))

    return answer

N = int(input())
M = int(input())
print(solution(N, M))