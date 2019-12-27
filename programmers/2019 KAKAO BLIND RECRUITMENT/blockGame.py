# 2019 KAKAO BLIND RECRUITMENT 블록 게임
# https://programmers.co.kr/learn/courses/30/lessons/42894

def solution(board):
    answer = 0
    N = len(board)
    cases = getCases()

    count = 1
    while count > 0:
        count = 0
        for i in range(N):
            for j in range(N):
                if(i <= N-2 and j <= N-3 and findAvail(i, j, 'h', board)):
                    count += 1
                elif(i <= N-3 and j <= N-2 and findAvail(i, j, 'v', board)):
                    count += 1
        answer += count

    return answer

def findAvail(r, c, typehv, board):
    zeroBlock = 0
    beforeBlock = 0
    if typehv == 'h':
        for i in range(r, r+2):
            for j in range(c, c+3):
                if(board[i][j] == 0):
                    if(isAvail(i, j, board)==False):return False
                    zeroBlock += 1
                    if(zeroBlock > 2): return False
                else:
                    if(beforeBlock != 0 and beforeBlock != board[i][j]): return False
                    beforeBlock = board[i][j]
        for i in range(r, r+2):
            for j in range(c, c+3):
                board[i][j] = 0
    elif typehv == 'v':
        for i in range(r, r+3):
            for j in range(c, c+2):
                if(board[i][j] == 0):
                    if(isAvail(i, j, board)==False):return False
                    zeroBlock += 1
                    if(zeroBlock > 2): return False
                else:
                    if(beforeBlock != 0 and beforeBlock != board[i][j]): return False
                    beforeBlock = board[i][j]
        for i in range(r, r+3):
            for j in range(c, c+2):
                board[i][j] = 0
    return True

def isAvail(r, c, board):
    for i in range(r):
        if(board[i][c] != 0):
            return False
    return True

def solution2(board):
    answer = 0
    cases = getCases()
    N = len(board)  # 행 수
    M = max(list(map(max, board)))  # 색깔 종류
    spare = [[0 for i in range(N)] for j in range(2)]
    board = spare + board + spare
    for i in range(len(board)):
        board[i] = [0, 0] + board[i] + [0, 0]
    iset = getIset(board)

    for j in range(len(board)):
        i = iset[j]
        if(i!=0):
            for k in range(1, M+1):
                sideCases = checkSide(i, j, k, board)
                for sc in sideCases:
                    if(sc[0] in cases):
                        curCase = sc[1]
                        if curCase == 0:
                            if (iset[j+2] < i-1):
                                continue
                        elif curCase == 1:
                            if (iset[j+2] < i):
                                continue
                        elif curCase == 2:
                            if (iset[j-2] < i):
                                continue
                        elif curCase == 3:
                            if (iset[j-2] < i+1):
                                continue
                        elif curCase == 4:
                            if (iset[j+1] < i-2):
                                continue
                        elif curCase == 5:
                            if (iset[j+1] < i):
                                continue
                        elif curCase == 6:
                            if (iset[j-1] < i):
                                continue
                        elif curCase == 7:
                            if (iset[j-1] < i-2):
                                continue
                        delCase(i, j, curCase, board)
                        answer += 1
    checkSide(10, 3, 2, board)

    return answer

def delCase(i, j, case, board):
    #print('del', i, j, case)
    if case == 0:
        for m in range(2):
            for n in range(3):
                board[i-m][j+n] = 0
    elif case == 1:
        for m in range(2):
            for n in range(3):
                board[i+m][j+n] = 0
    elif case == 2:
        for m in range(2):
            for n in range(3):
                board[i+m][j-n] = 0
    elif case == 3:
        for m in range(2):
            for n in range(3):
                board[i-m][j-n] = 0
    elif case == 4:
        for m in range(3):
            for n in range(2):
                board[i-m][j+n] = 0
    elif case == 5:
        for m in range(3):
            for n in range(2):
                board[i+m][j+n] = 0
    elif case == 6:
        for m in range(3):
            for n in range(2):
                board[i+m][j-n] = 0
    elif case == 7:
        for m in range(3):
            for n in range(2):
                board[i-m][j-n] = 0

def checkSide(i, j, c, board):
    case1 = [[isColor(board[i-1][j], c), isColor(board[i-1][j+1], c), isColor(board[i-1][j+2], c)],
            [isColor(board[i][j], c), isColor(board[i][j+1], c), isColor(board[i][j+2], c)]]
    case2 = [[isColor(board[i][j], c), isColor(board[i][j + 1], c), isColor(board[i][j + 2], c)],
             [isColor(board[i + 1][j], c), isColor(board[i + 1][j + 1], c), isColor(board[i + 1][j + 2], c)]]
    case3 = [[isColor(board[i][j - 2], c), isColor(board[i][j - 1], c), isColor(board[i][j], c)],
             [isColor(board[i + 1][j - 2], c), isColor(board[i + 1][j - 1], c), isColor(board[i + 1][j], c)]]
    case4 = [[isColor(board[i - 1][j - 2], c), isColor(board[i - 1][j - 1], c), isColor(board[i - 1][j], c)],
             [isColor(board[i][j - 2], c), isColor(board[i][j - 1], c), isColor(board[i][j], c)]]
    case5 = [[isColor(board[i-2][j], c), isColor(board[i-2][j+1], c)],
             [isColor(board[i-1][j], c), isColor(board[i-1][j+1], c)],
             [isColor(board[i][j], c), isColor(board[i][j+1], c)]]
    case6 = [[isColor(board[i][j], c), isColor(board[i][j + 1], c)],
             [isColor(board[i + 1][j], c), isColor(board[i + 1][j + 1], c)],
             [isColor(board[i + 2][j], c), isColor(board[i + 2][j + 1], c)]]
    case7 = [[isColor(board[i][j - 1], c), isColor(board[i][j], c)],
             [isColor(board[i + 1][j - 1], c), isColor(board[i + 1][j], c)],
             [isColor(board[i + 2][j - 1], c), isColor(board[i + 2][j], c)]]
    case8 = [[isColor(board[i - 2][j - 1], c), isColor(board[i - 2][j], c)],
             [isColor(board[i - 1][j - 1], c), isColor(board[i - 1][j], c)],
             [isColor(board[i][j - 1], c), isColor(board[i][j], c)]]
    cases = [case1, case2, case3, case4, case5, case6, case7, case8]
    for i in range(len(cases)):
        cases[i] = (cases[i], i)
    return cases

def isColor(origin, c):
    return 1 if origin == c else -1 if origin != 0 else 0

def getIset(board):
    iset = []
    N = len(board)
    for j in range(N):
        idx = 0
        for i in range(N):
            if (board[i][j] != 0):
                break
            idx += 1
        if(idx == N):
            idx = 0
        iset.append(idx)
    return iset

def getCases():
    cases = [
        [[1, 0, 0],
         [1, 1, 1]],
        [[0, 1, 0],
         [1, 1, 1]],
        [[0, 0, 1],
         [1, 1, 1]],
        [[1, 0],
         [1, 0],
         [1, 1]],
        [[0, 1],
         [0, 1],
         [1, 1]]
    ]
    return cases


print(solution([[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,4,0,0,0],
                [0,0,0,0,0,4,4,0,0,0],
                [0,0,0,0,3,0,4,0,0,0],
                [0,0,0,2,3,0,0,0,5,5],
                [1,2,2,2,3,3,0,0,0,5],
                [1,1,1,0,0,0,0,0,0,5]]))
