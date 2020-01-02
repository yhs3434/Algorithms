# 찾아라 프로그래밍 마에스터 - 게임 맵 최단거리
# https://programmers.co.kr/learn/courses/30/lessons/1844

import queue

def solution(maps):
    answer = float('inf')

    N = len(maps)
    M = len(maps[0])
    q = queue.Queue()

    if(maps[N-2][M-1]==0 and maps[N-1][M-2]==0):
        return -1
    s = [[(float('inf') if (maps[i][j]==1) else 0) for j in range(M)] for i in range(N)]
    s[0][0] = 1

    stack = [(0, 0)]
    q.put((0, 0))
    while q.empty()==False:
        cur = q.get()
        r = cur[0]
        c = cur[1]
        if(c==(M-1) and r==(N-1)):
            if(s[r][c] < answer):
                answer = s[r][c]
        if(s[r][c] < answer):
            if(c>0 and s[r][c-1] != 0):
                if(s[r][c]+1 < s[r][c-1]):
                    s[r][c-1] = s[r][c] + 1
                    q.put((r, c-1))
            if(c<(M-1) and s[r][c+1] != 0):
                if(s[r][c]+1 < s[r][c+1]):
                    s[r][c+1] = s[r][c] + 1
                    q.put((r, c+1))
            if(r>0 and s[r-1][c] != 0):
                if(s[r][c]+1 < s[r-1][c]):
                    s[r-1][c] = s[r][c] + 1
                    q.put((r-1, c))
            if (r < (N-1) and s[r+1][c] != 0):
                if (s[r][c] + 1 < s[r + 1][c]):
                    s[r + 1][c] = s[r][c] + 1
                    q.put((r + 1, c))

    if(s[N-1][M-1] >= float('inf')):
        answer = -1
    else:
        answer = s[N-1][M-1]

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))