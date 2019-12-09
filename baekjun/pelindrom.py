# 무-팰린드롬 숫자
# https://www.acmicpc.net/problem/6289

def solution(numbers):
    x = int(numbers[0])
    y = int(numbers[1])
    count = 0
    for num in range(x, y+1):
        if(isPelindrom(num)==False):
            count+=1
    return count

def isPelindrom(num):
    numStr = str(num)
    numLen = len(numStr)
    flag = False
    for i in range(2, 4):
        for j in range(numLen-i+1):
            if(isSame(numStr[j:j+i])==True):
                flag=True
                break
    return flag

def isSame(numStr):
    flag = True
    for i in range(len(numStr)):
        j = len(numStr)-i-1
        if(i>j):
            break
        if(numStr[i]!=numStr[j]):
            flag = False
            break
    return flag

prb = input().split(' ')
print(solution(prb))