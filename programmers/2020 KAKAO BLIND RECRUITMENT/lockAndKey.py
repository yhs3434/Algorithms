# 2020 KAKAO BLIND RECRUITMENT 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

def solution(key, lock):
    answer = False

    newLock = expandLock(key, lock)
    newLockLen = len(newLock)
    kLen = len(key)
    expandLen = kLen - 1

    for i in range(newLockLen - expandLen):
        for j in range(newLockLen - expandLen):
            newKey = turnKey(key)
            for k in range(4):
                newKey = turnKey(newKey)
                if combineKeyLock(i, j, newKey, newLock):
                    answer = True
                    return answer
    return answer

def combineKeyLock(r, c, key, lock):
    kLen = len(key)
    lLen = len(lock)
    expandLen = kLen - 1
    newLock = [[lock[i][j] for j in range(lLen)] for i in range(lLen)]
    for i in range(kLen):
        for j in range(kLen):
            if newLock[r+i][c+j] == key[i][j]:
                if r+i >= expandLen and r+i < lLen-expandLen and c+j >= expandLen and c+j < lLen-expandLen:
                    return False
            else:
                newLock[r+i][c+j] = 1
    if isRight(key, newLock):
        return True
    else:
        return False

def isRight(key, lock):
    kLen = len(key)
    lLen = len(lock)
    expandLen = kLen - 1
    sumVal = 0
    for i in range(lLen-2*expandLen):
        sumVal += sum(lock[i+expandLen][expandLen: lLen-expandLen])
    if sumVal == (lLen-2*expandLen)**2:
        return True
    else:
        return False

def expandLock(key, lock):
    kLen = len(key)
    expandLen = kLen - 1
    lockLen = len(lock)
    newLockLen = len(lock) + 2*expandLen
    newLock = [[0 for j in range(newLockLen)] for i in range(newLockLen)]
    for i in range(lockLen):
        for j in range(lockLen):
            newLock[i+expandLen][j+expandLen] = lock[i][j]
    return newLock

def turnKey(key):
    kLen = len(key)
    newKey = [[0 for i in range(kLen)] for j in range(kLen)]
    for i in range(kLen):
        for j in range(kLen):
            newKey[i][j] = key[kLen-j-1][i]
    return newKey

def moveKey(n, m, key, kLen):
    newKey = [[0 for i in range(kLen)] for j in range(kLen)]
    for i in range(kLen):
        for j in range(kLen):
            if i+n<kLen and j+m<kLen and i+n>=0 and j+m>=0:
                newKey[i+n][j+m] = key[i][j]
    return newKey

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
