# 전깃줄
# https://www.acmicpc.net/problem/2565

def solution(n, wires):
    answer = 0

    arr = []
    liss = []
    for i in range(n):
        arr.append(wires[i][1])
    dp = [0 for i in range(n)]
    dp[0] = 1
    for i in range(1, n):
        maxVal = 0
        for j in range(i):
            if arr[j] < arr[i]:
                if dp[j] > maxVal:
                    maxVal = dp[j]
        dp[i] = maxVal + 1
    return n - max(dp)

n = int(input())
wires = []
for xxx in range(n):
    wire = tuple(map(int, input().split(' ')))
    wires.append(wire)
wires.sort()
print(solution(n, wires))