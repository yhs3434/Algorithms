# 서머코딩 / 윈터코딩 (~2018) - 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978

import queue

def solution(N, road, K):
    answer = 0
    q = queue.Queue()
    visit = {}
    for i in range(1, N+1):
        visit[i] = {}
    towns = [float('inf') for i in range(N+1)]
    for r in road:
        a = r[0]
        b = r[1]
        if b not in visit[a]:
            visit[a][b] = r[2]
        else:
            if r[2] < visit[a][b]:
                visit[a][b] = r[2]
        if a not in visit[b]:
            visit[b][a] = r[2]
        else:
            if r[2] < visit[b][a]:
                visit[b][a] = r[2]
    visited = []
    q.put((1, 0))
    while not q.empty():
        cur = q.get()
        cTown = cur[0]
        cCnt = cur[1]
        if cCnt < towns[cTown]:
            towns[cTown] = cCnt
        visited.append(cTown)
        for nTown in visit[cTown]:
            if cCnt + visit[cTown][nTown] < towns[nTown]:
                q.put((nTown, cCnt+visit[cTown][nTown]))
    for time in towns:
        if time <= K:
            answer += 1

    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, 	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))