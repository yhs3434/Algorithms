# 2019 KAKAO BLIND RECRUITMENT 후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890

import queue

def solution(relation):
    answer = 0
    keyLen = len(relation[0])

    keys = []
    avails = []
    q = queue.Queue()
    q.put([])
    for i in range(1, keyLen+1):
        temp2 = []
        while q.empty()!=True:
            cur = q.get()
            for j in range(keyLen):
                if(len(cur)==0 or j>cur[-1]):
                    temp = cur[:]
                    temp.append(j)
                    temp2.append(temp)
        for t in temp2:
            avails.append(t)
            q.put(t)
    beforeLen = 0
    tempKey = []
    for avail in avails:
        if(beforeLen != len(avail)):
            while tempKey:
                keys.append(tempKey.pop())
        beforeLen = len(avail)
        temp = []
        curKey = ''
        for a in avail:
            a = str(a)

        flag = False
        for key in keys:
            if(len(set(avail)&set(key))==len(key)):
                flag = True
                break
        if(flag):
            continue
        for r in relation:
            tuple = ''
            for a in avail:
                tuple += str(r[a])+','
            temp.append(tuple)
        if(len(temp) == len(set(temp))):
            tempKey.append(avail)
            answer += 1

    return answer


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution([['a','b','c'], [1,'b','c'], ['a','b',4], ['a',5,'c']]))
print(solution([['a','b','c']]))
print(solution([['1'], ['3'], ['1']]))
print(solution([[1,2,10,11], [2,3,10,12], [1,3,10,12], [2, 4, 9, 12]]))