def solution(left, right):
    answer = 0
    leftLen = len(left)
    rightLen = len(right)

    map = [[-1 for i in range(rightLen+1)] for i in range(leftLen+1)]
    map[0][0] = 0
    for i in range(leftLen):
        for j in range(rightLen):
            if(map[i][j]!=-1):
                if(right[j] < left[i]):
                    if(map[i][j+1]<map[i][j]+right[j]):
                        map[i][j+1] = map[i][j] + right[j]
                    if(map[i+1][j]<map[i][j]):
                        map[i+1][j] = map[i][j]
                    if(map[i+1][j+1]<map[i][j]):
                        map[i+1][j+1] = map[i][j]
                else:
                    if (map[i + 1][j] < map[i][j]):
                        map[i + 1][j] = map[i][j]
                    if (map[i + 1][j + 1] < map[i][j]):
                        map[i + 1][j + 1] = map[i][j]
    for row in map:
        if(answer < row[-1]):
            answer = row[-1]
    return answer

print(solution([3, 2, 5], [2, 4, 1]))