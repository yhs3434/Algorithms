# 싸이클
# https://www.acmicpc.net/problem/2526
# https://github.com/yhs3434/Algorithms

n, p = map(int, input().split(' '))

arr = []
visited = [False] * p
c = n
idx = 0
while True:
    c = c*n%p
    if visited[c]:
        idx = arr.index(c)
        break
    else:
        arr.append(c)
        visited[c] = True

print(len(arr)-idx)