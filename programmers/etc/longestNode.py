# 그래프 - 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189

import queue
import numpy as np

def solution(n, edge):
    answer = 0

    visit = {}
    for e in edge:
        if e[0] not in visit:
            visit[e[0]] = set([e[1]])
        else:
            visit[e[0]].add(e[1])
        if e[1] not in visit:
            visit[e[1]] = set([e[0]])
        else:
            visit[e[1]].add(e[0])

    scores = [0 for i in range(n+1)]

    q = queue.Queue()
    q.put((1, 0))
    visited = set([1])
    while not q.empty():
        cur = q.get()
        cNode = cur[0]
        cCnt = cur[1]
        scores[cNode] = cCnt
        for i in visit[cNode]:
            if i not in visited:
                q.put((i, cCnt+1))
                visited.add(i)

    maxScore = max(scores)
    for score in scores:
        if score == maxScore:
            answer += 1
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))