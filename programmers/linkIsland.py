# 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861

from heapq import heappush, heappop
import queue

def solution(n, costs):
    answer = 0

    heap = []
    numOfLink = n-1

    map = [[0 for i in range(n)] for i in range(n)]
    for c in costs:
        heappush(heap, (c[2], c[0], c[1]))

    while numOfLink>0:
        curItem = heappop(heap)
        map[curItem[1]][curItem[2]] = curItem[0]
        map[curItem[2]][curItem[1]] = curItem[0]
        if(isCycle(map, curItem[1])):
            map[curItem[1]][curItem[2]] = 0
            map[curItem[2]][curItem[1]] = 0
        else:
            answer += curItem[0]
            numOfLink -= 1

    return answer

def isCycle(map, idx):
    q = queue.Queue()
    n = len(map)
    flag = False
    q.put((idx,-1))
    while(q.empty()!=True):
        curq = q.get()
        curIdx = curq[0]
        beforeIdx = curq[1]
        temp = []
        for i in range(n):
            if(i!=beforeIdx and map[curIdx][i]>0):
                if(i==idx):
                    flag = True
                temp.append(i)
        if (flag):
            break
        while temp:
            q.put((temp.pop(), curIdx))
    return flag

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))