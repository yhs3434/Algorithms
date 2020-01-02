# 연습문제 - 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = 0

    nBin = bin(n)
    binArr = []

    for i in range(2, len(nBin)):
        binArr.append(int(nBin[i]))
    oneCnt = binArr.count(1)
    binArr = plusOne(binArr)
    while binArr.count(1) != oneCnt:
        binArr = plusOne(binArr)

    delim = 1
    for i in range(len(binArr)):
        i = len(binArr) - i - 1
        answer += (binArr[i] * delim)
        delim *= 2

    return answer

def plusOne(binArrOrigin):
    binArr = binArrOrigin[:]
    for i in range(len(binArr)):
        i = len(binArr) - i - 1
        if binArr[i] == 0:
            binArr[i] = 1
            break
        else:
            binArr[i] = 0
    if binArr.count(1) == 0:
        binArr = [1] + binArr
    return binArr

print(solution(78))
print(solution(15))
