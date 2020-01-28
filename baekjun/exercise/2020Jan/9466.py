# 텀 프로젝트
# https://www.acmicpc.net/problem/9466
# https://github.com/yhs3434/Algorithms

from collections import deque
import sys
rl = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(rl().rstrip())
    arr = [0] + list(map(int, rl().rstrip().split(' ')))

    cnt = 0
    q = deque()
    visited = [False] * (n + 1)

    for i in range(1, n+1):
        if not visited[i]:
            start = i
            q.append(start)

            visited2 = [i]
            idx = 0
            visited[i] = True

            flag = False
            while q:
                cur = q.popleft()
                if not visited[arr[cur]]:
                    q.append(arr[cur])
                    visited[arr[cur]] = True
                    visited2.append(arr[cur])
                else:
                    if arr[cur] in visited2:
                        idx = visited2.index(arr[cur])
                    flag = True
            if flag:
                print(visited2)
                print('team', visited2[idx:])
                cnt += idx
    print(cnt)