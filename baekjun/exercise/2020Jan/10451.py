# 순열 사이클
# https://www.acmicpc.net/problem/10451
# https://github.com/yhs3434/Algorithms

t = int(input())
for _ in range(t):
    N = int(input())
    arr = [0] + list(map(int, input().split(' ')))
    cnt = 0
    visited = [False] * (N+1)

    for s in range(1, N+1):
        if not visited[s]:
            newVisited = [False] * (N+1)
            here = s
            there = arr[s]
            flag = False
            while not visited[there]:
                newVisited[here] = True
                visited[here] = True
                there = arr[here]
                here = there
                if newVisited[there]:
                    flag = True
            if flag:
                cnt += 1
    print(cnt)
