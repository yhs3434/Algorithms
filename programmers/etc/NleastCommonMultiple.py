# N개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    answer = 0

    for i in range(len(arr)-1):
        n1 = arr[i]
        n2 = arr[i+1]
        comm = getCommon(n1, n2)
        arr[i+1] = (n1//comm) * n2
    answer = arr[-1]
    return answer

def getCommon(n1, n2):
    comm = subAbs(n1, n2)
    minVal = min(n1, n2)
    while comm != minVal:
        temp = comm
        comm = subAbs(minVal, comm)
        minVal = temp
    return comm

def subAbs(n1, n2):
    return n1 - n2 if n1 >= n2 else n2 - n1

print(solution([2,6,8,14]))
print(solution([1,2,3]))

getCommon(24,28)