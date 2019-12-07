def solution(land, height):
    answer = 0
    sum = [float('inf')]

    land_copy = [[0 for i in range(len(land[0]))] for i in range(len(land))]
    for i in range(len(land)):
        for j in range(len(land[0])):
            land_copy[i][j] = {'val': land[i][j], 'land': -1}

    land_count = 0
    for i in range(len(land_copy)):
        for j in range(len(land_copy[0])):
            if(land_copy[i][j]['land']==-1):
                makeLand(land_count, height, i, j, land_copy)
                land_count += 1
    ladderMap = [[0 for i in range(land_count)] for i in range(land_count)]

    ladderCase(sum, 0, ladderMap, land_count-1, land_copy)
    answer = sum[0]

    return answer

def makeLadder(ladderMap, land):

    sum = 0
    for i in range(len(ladderMap)):
        for j in range(i+1, len(ladderMap[0])):
            if(ladderMap[i][j]==1):
                sum+=getLadderMax(i,j,land)

    return sum

def getLadderMax(x,y,land):
    minVal = float('inf')
    for i in range(len(land)):
        for j in range(len(land[0])):
            if(land[i][j]['land']==x):
                if ((i - 1) >= 0):
                    if(land[i-1][j]['land']==y):
                        if(getAbs(land[i-1][j]['val'], land[i][j]['val'])<minVal):
                            minVal = getAbs(land[i-1][j]['val'], land[i][j]['val'])
                if ((i + 1) < len(land)):
                    if (land[i + 1][j]['land'] == y):
                        if (getAbs(land[i + 1][j]['val'], land[i][j]['val']) < minVal):
                            minVal = getAbs(land[i + 1][j]['val'], land[i][j]['val'])
                if ((j - 1) >= 0):
                    if (land[i][j-1]['land'] == y):
                        if (getAbs(land[i][j-1]['val'], land[i][j]['val']) < minVal):
                            minVal = getAbs(land[i][j-1]['val'], land[i][j]['val'])
                if ((j + 1) < len(land[0])):
                    if (land[i][j+1]['land'] == y):
                        if (getAbs(land[i][j+1]['val'], land[i][j]['val']) < minVal):
                            minVal = getAbs(land[i][j+1]['val'], land[i][j]['val'])
    return minVal

def ladderCase(sum, count, ladderMap, ladderMax, land):
    if(count==ladderMax):
        resultVal = makeLadder(ladderMap, land)
        if(resultVal!=float('inf') and resultVal<sum[0]):
            sum[0] = resultVal
        return
    ladderMap_copy = [[0 for i in range(len(ladderMap))] for i in range(len(ladderMap))]
    for i in range(len(ladderMap)):
        for j in range(len(ladderMap)):
            ladderMap_copy[i][j] = ladderMap[i][j]

    for i in range(ladderMax+1):
        for j in range(i+1, ladderMax+1):
            if(i==j):
                continue
            else:
                if(getLadderNum(i, ladderMap_copy)<2 and ladderMap_copy[i][j] != 1):
                    ladderMap_copy[i][j]=1
                    ladderMap_copy[j][i]=1
                    ladderCase(sum, count+1, ladderMap_copy, ladderMax, land)
                    ladderMap_copy[i][j] = 0
                    ladderMap_copy[j][i] = 0
    return

def makeLand(l, height, a, b, land):
    land[a][b]['land'] = l
    if((a-1)>=0):
        if(getAbs(land[a-1][b]['val'], land[a][b]['val'])<=height):
            if(land[a-1][b]['land']==-1):
                makeLand(l, height, a-1, b, land)
    if((a+1)<len(land)):
        if (getAbs(land[a + 1][b]['val'], land[a][b]['val']) <= height):
            if (land[a + 1][b]['land'] == -1):
                makeLand(l, height, a + 1, b, land)
    if((b-1)>=0):
        if (getAbs(land[a][b-1]['val'], land[a][b]['val']) <= height):
            if (land[a][b-1]['land'] == -1):
                makeLand(l, height, a, b-1, land)
    if((b+1)<len(land[0])):
        if (getAbs(land[a][b+1]['val'], land[a][b]['val']) <= height):
            if (land[a][b+1]['land'] == -1):
                makeLand(l, height, a, b+1, land)
    return

def getAbs(val1, val2):
    result = val1-val2
    if(result>=0):
        return result
    else:
        return -result

def getLadderNum(l, ladder_map):
    return ladder_map[l].count(1)

def getTotalLadderNum(ladder_map):
    sum = 0
    for i in range(len(ladder_map)):
        sum += ladder_map[i].count(1)
    return sum

print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))