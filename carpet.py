def solution(brown, red):
    answer = []

    redAvailable = getFactorization(red)
    brownAvailable = getBrown(redAvailable)

    idx = 0
    for i in range(len(redAvailable)):
        if(brown==brownAvailable[i]):
            idx=i
            break
    answer = redAvailable[idx]
    answer[0]+=2
    answer[1]+=2
    return answer

def getFactorization(red):
    arr = []
    for i in range(1, int(red**(1/2))+1):
        if(red%i==0):
            height = i
            width = red//i
            arr.append([width, height])
    return arr

def getBrown(available):
    arr = []
    for a in available:
        width = a[0]
        height = a[1]
        brown = 2*(width+height)+4
        arr.append(brown)
    return arr

solution(24, 24)