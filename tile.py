def solution(n):
    map = [[0 for i in range(n)] for i in range(3)]
    answer = [0]
    putTileHorizontal(map, map, 0, 0, answer)
    putTileVertical(map, map, 0, 0, answer)
    return int(answer[0]%1000000007);

def putTileHorizontal(originalMap, map, a, b, answer):
    if(a>=3 or (a==2 and b==len(map[0]))):
        if(isFull(map)):
            answer[0] += 1
        return

    map_copy = [[0 for i in range(len(map[0]))] for i in range(len(map))]
    for i in range(len(map)):
        for j in range(len(map[0])):
            map_copy[i][j] = map[i][j]

    horizonLength = len(map[0])
    verticalLength = len(map)
    if((b+1) >= horizonLength or map[a][b+1] == 1):
        return False
    else:
        map_copy[a][b] = 1
        map_copy[a][b+1] = 1
        a_index = a
        b_index = b
        while(True):
            b_index += 1

            if(b_index==horizonLength):
                a_index += 1
                b_index = 0
                if(a_index == verticalLength):
                    if (isFull(map_copy)):
                        answer[0] += 1
                    return
                if (map_copy[a_index][b_index] == 1):
                    continue
            if (map_copy[a_index][b_index] == 1):
                continue
            break
        putTileHorizontal(originalMap, map_copy, a_index, b_index, answer)
        putTileVertical(originalMap, map_copy, a_index, b_index, answer)
        return True

def putTileVertical(originalMap, map, a, b, answer):
    if(b>=len(map[0]) and a>=2):
        if(isFull(map)):
            answer[0] += 1
        return

    map_copy = [[0 for i in range(len(map[0]))] for i in range(len(map))]
    for i in range(len(map)):
        for j in range(len(map[0])):
            map_copy[i][j] = map[i][j]

    horizonLength = len(map[0])
    verticalLength = len(map)
    if((a+1) >= verticalLength or map[a+1][b] == 1):
        return False
    else:
        map_copy[a][b] = 1
        map_copy[a+1][b] = 1
        a_index = a
        b_index = b
        while(True):
            b_index += 1

            if(b_index==horizonLength):
                a_index += 1
                b_index = 0
                if(a_index == verticalLength):
                    if (isFull(map_copy)):
                        answer[0] += 1
                    return
                if (map_copy[a_index][b_index] == 1):
                    continue
            if (map_copy[a_index][b_index] == 1):
                continue
            break
        putTileHorizontal(originalMap, map_copy, a_index, b_index, answer)
        putTileVertical(originalMap, map_copy, a_index, b_index, answer)
        return True

def isFull(map):
    flag = True
    for i in range(len(map)):
        for j in range(len(map[0])):
            if(map[i][j] != 1):
                flag=False
                break;
    return flag

print(solution(12))