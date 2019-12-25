# 2018 KAKAO BLIND RECRUITMENT [1차] 프렌즈4블록
# https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    answer = 0

    maps = [[board[i][j] for j in range(n)] for i in range(m)]
    count = [0]
    stagePart(m, n, maps, count)
    answer = count[0]
    return answer

def stagePart(m, n, maps, count):
    removes = []
    for i in range(m - 1):
        for j in range(n - 1):
            arr = [maps[i][j], maps[i][j + 1], maps[i + 1][j], maps[i + 1][j + 1]]
            if (arr[0] != ' ' and len(set(arr)) == 1):
                removes.extend([str(i) + ',' + str(j), str(i) + ',' + str(j + 1), str(i + 1) + ',' + str(j),
                                str(i + 1) + ',' + str(j + 1)])
    removes = list(set(removes))
    newRemoves = []
    for i in range(len(removes)):
        remove = removes[i]
        remove = remove.split(',')
        remove = list(map(int, remove))
        newRemoves.append(remove)
    newRemoves.sort(key=lambda key:key[1])
    newRemoves.sort(key=lambda key:key[0])

    for remove in newRemoves:
        r = remove[0]
        c = remove[1]
        for i in range(r + 1):
            i = r - i
            if (i > 0):
                maps[i][c] = maps[i - 1][c]
            else:
                maps[i][c] = ' '
    if(len(removes)!=0):
        count[0] += len(removes)
        stagePart(m, n, maps, count)


print(solution(4,5,['CCBDE', 'AAADE', 'AAABF', 'CCBBF'] ))
print(solution(6,6,['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))