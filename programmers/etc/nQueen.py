# 연습문제 - N-Queen
# https://programmers.co.kr/learn/courses/30/lessons/12952

import queue

def solution(n):
    answer = 0

    q = queue.Queue()
    q.put((0, [i for i in range(n)], []))  # (행, 방문 열, 놓은 행열)
    while not q.empty():
        cur = q.get()
        #print(cur)
        r = cur[0]
        visitC = cur[1]
        queens = cur[2]
        if r == n:
            answer += 1
        for c in visitC:
            flag = True
            for j in range(1, r+1):
                if (c-j >=0 and queens[r-j]==c-j) or (c+j < n and queens[r-j] == c+j):
                    flag = False
            if flag:
                newVisitC = visitC[:]
                newVisitC.remove(c)
                q.put((r+1, newVisitC, queens+[c]))

    return answer

print(solution(4))