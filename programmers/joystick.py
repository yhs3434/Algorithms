# 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860

import queue

def solution2(name):
    answer = 0

    length = len(name)
    idx = 0
    curStr = 'A'*length
    arr = [0 for i in range(length)]
    while(curStr!=name):
        minVal = float('inf')
        minIdx = 0
        for i in range(length):
            if(name[i]==curStr[i]):
                continue
            absValue = absVal(ord(name[i]) - ord(curStr[i]))
            absValue = absValue if absValue<(26-absValue) else 26-absValue
            arr[i] = absValue+absVal(i-idx)
            print(arr, i, idx)
            if(arr[i]<minVal and arr[i]!=0):
                minIdx = i
                minVal = arr[minIdx]

        idx = minIdx
        answer += arr[idx]
        arr[idx] = 0
        curStr = curStr[:idx]+name[idx]+curStr[idx+1:]
        print(curStr, answer)

    return answer

def solution3(name):
    answer1 = 0
    answer2 = 0

    length = len(name)
    curStr = 'A'*length
    ordA = ord('A')
    curArr = [absVal(ord(name[i]) - ordA) for i in range(length)]
    for i in range(length):
        val = curArr[i]
        curArr[i] = val if val<(26-val) else 26-val

    idx1 = 0
    idx2 = 0

    for i in range(length):
        answer1 += curArr[i]
        answer2 += curArr[-i]
        if(curArr[i]!=0):
            idx1 = i
        if(curArr[-i]!=0):
            idx2 = i
    answer = answer1+idx1 if (answer1+idx1)<(answer2+idx2) else answer2+idx2

    return answer

def solution(name):
    answer = 0
    q = queue.Queue()
    length = len(name)
    curStr = 'A'*length
    ordA = ord('A')
    curArr = [absVal(ord(name[i]) - ordA) for i in range(length)]
    for i in range(length):
        val = curArr[i]
        curArr[i] = val if val < (26 - val) else 26 - val
    q.put((curArr, 0, 0))
    saveArr = []
    for i in range(length):
        flag = True
        while (q.empty()!=True):
            temp = q.get()
            tempArr = temp[0]
            tempIdx = temp[1]
            tempAnswer = temp[2]
            tempAnswer += tempArr[tempIdx]
            tempArr[tempIdx] = 0
            if(sum(tempArr)==0):
                flag = False
                answer = tempAnswer
                break
            saveArr.append((tempArr[:], tempIdx - 1, tempAnswer))
            saveArr.append((tempArr[:], tempIdx + 1, tempAnswer))
        if(flag==False):
            answer += i
            break
        while saveArr:
            q.put(saveArr.pop())
    return answer

def absVal(num):
    if(num<0):
        return -num
    else:
        return num

print(solution("JAZ"))
print(solution("JEROEN"))