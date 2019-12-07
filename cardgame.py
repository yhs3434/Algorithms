def solution(left, right):
    answer = 0

    leftLen = len(left)
    rightLen = len(right)

    map = [[0 for i in range(rightLen+1)] for i in range(leftLen+1)]
    doGame(0, left, right, 0, 0, map)

    maxVal = 0
    for row in map:
        if(maxVal < row[-1]):
            maxVal = row[-1]
    answer = maxVal

    return answer

def doGame(val, left, right, leftIdx, rightIdx, map):
    if(leftIdx>=len(left) or rightIdx>=len(right)):
        if (map[leftIdx][rightIdx] < val):
            map[leftIdx][rightIdx] = val
        return
    if(map[leftIdx][rightIdx] < val):
        map[leftIdx][rightIdx] = val
    leftCard = left[leftIdx]
    rightCard = right[rightIdx]

    if(rightCard < leftCard):
        doGame(val+rightCard, left, right, leftIdx, rightIdx+1, map)
        doGame(val, left, right, leftIdx+1, rightIdx, map)
        doGame(val, left, right, leftIdx+1, rightIdx+1, map)
    else:
        doGame(val, left, right, leftIdx + 1, rightIdx, map)
        doGame(val, left, right, leftIdx + 1, rightIdx + 1, map)

print(solution([3, 2, 5, 7, 8, 10, 2], [2, 4, 1, 9 , 5, 3, 10, 50, 2]))