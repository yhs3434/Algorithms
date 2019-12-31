# 2020 KAKAO BLIND RECRUITMENT 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062

import queue
from itertools import permutations
import numpy as np

def solution(n, weak, dist):
    answer = 101
    wLen = len(weak)
    dLen = len(dist)
    q = queue.Queue()

    for k in range(wLen):
        newWeak = weak[k:]
        for kk in range(k):
            newWeak.append(weak[kk] + n)
        q.put((newWeak, []))
        while not q.empty():
            cur = q.get()
            cWeak = cur[0]
            cDist = cur[1]
            if len(cWeak) == 0:
                if len(cDist) < answer:
                    answer = len(cDist)
            elif len(cDist) >= answer:
                while not q.empty():
                    q.get()
                break
            else:
                for i in range(dLen):
                    if i not in cDist:
                        cnt = 0
                        d = dist[i]
                        while cWeak[cnt] <= cWeak[0] + d:
                            cnt += 1
                            if cnt >= len(cWeak):
                                break
                        q.put((cWeak[cnt:], cDist+[i]))

    if answer == 101:
        answer = -1
    return answer

def solution2(n, weak, dist):
    answer = 101
    wLen = len(weak)
    dLen = len(dist)
    q = queue.Queue()

    dist.sort(reverse=True)
    comFriends = [i for i in range(dLen)]
    comWeak = [i for i in range(wLen)]
    board = [[0 for i in range(wLen)] for j in range(wLen)]
    bLen = len(board)
    for i in range(wLen):
        for j in range(wLen):
            board[i][j] = getDist(weak[i], weak[j], n)

    fCnt = 0
    while fCnt<dLen and answer==101:
        fCnt += 1
        curDists = dist[:fCnt]
        q.put(([], []))     # (사용한 친구, 확인한 벽)
        weaks = []
        while not q.empty():
            cur = q.get()
            usedFriends = cur[0]
            checkedWeak = cur[1]
            checkedWeak.sort()
            unCheckedWeak = comWeak[:]
            for cw in checkedWeak:
                unCheckedWeak.remove(cw)
            if answer != 101:
                break
            else:
                for i in range(len(curDists)):
                    if i not in usedFriends:
                        d = curDists[i]
                        maxIdxs = []
                        maxLength = 1
                        for r in unCheckedWeak:
                            mCnt = 0
                            for c in unCheckedWeak:
                                if board[r][c]<=d:
                                    mCnt += 1
                            if mCnt >= maxLength:
                                if mCnt == maxLength:
                                    maxIdxs.append(r)
                                else:
                                    maxIdxs = [r]
                                maxLength = mCnt

                        for maxIdx in maxIdxs:
                            checked = []
                            for c in unCheckedWeak:
                                if board[maxIdx][c] <= d:
                                    checked.append(c)

                            rCheckedWeak = checkedWeak + checked
                            rCheckedWeak.sort()
                            if comWeak == rCheckedWeak:
                                answer = fCnt
                            else:
                                rUsedFriends = usedFriends + [i]
                                rUsedFriends.sort()
                                print(rUsedFriends, curDists, weaks, fCnt)
                                if (rUsedFriends, rCheckedWeak) not in weaks:
                                    weaks.append((rUsedFriends, rCheckedWeak))
                                    q.put((rUsedFriends, rCheckedWeak))

    if answer == 101:
        answer = -1
    return answer

def getDist(n1, n2, n):
    result = n1 - n2
    if result < 0:
        result += n
    return result


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]	))
print(solution(12, 	[1, 3, 4, 9, 10], 	[3, 5, 7]))
print(solution(120, [1,115,117,119], [2,2,1,1]))
#print(solution(20, 	[1, 3, 4, 9, 10], 	[1,2,1,3,2]))