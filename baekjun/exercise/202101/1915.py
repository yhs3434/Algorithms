n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input()))))

dp = [[0] * m for _ in range(n)]
if arr[0][0] == 1:
    dp[0][0] = 1
for r in range(n):
    for c in range(m):
        if arr[r][c] == 1:
            dp[r][c] = 1
        if 0 <= r-1 and 0 <= c-1:
            if arr[r-1][c-1] == arr[r-1][c] == arr[r][c-1] == 1:
                if dp[r-1][c-1] != 1 and dp[r-1][c] != 1 and dp[r][c-1] != 1:
                    dp[r][c] = (int(min(dp[r-1][c-1], dp[r][c-1], dp[r-1][c]) ** (1/2)) + 1) ** 2
                else:
                    dp[r][c] = 4

answer = 0
for row in dp:
    answer = max(answer, max(row))
print(answer)
