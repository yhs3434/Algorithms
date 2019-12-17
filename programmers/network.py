# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    length = len(computers)

    stack = []

    for i in range(length):
        if(computers[i][i] != 0):
            answer += 1
            stack.append(i)
            while stack:
                c = stack.pop()
                for j in range(length):
                    if(c!=j and computers[c][j]==1):
                        stack.append(j)
                    computers[c][j] = 0
    return answer

print(solution(4, [[1,0,0,1],[0,1,1,1],[0,1,1,0],[1,1,0,1]]))