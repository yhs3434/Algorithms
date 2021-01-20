N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1

    sumVal = 0
    for r in range(N):
        for c in range(M):
            if j <= c <= y and i <= r <= x:
                sumVal += arr[r][c]
    print(sumVal)