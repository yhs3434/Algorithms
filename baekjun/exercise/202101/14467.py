N = int(input())
cnt = 0
cows = [-1] * (11)
for _ in range(N):
    cow, pos = map(int, input().split())
    if cows[cow] == -1:
        cows[cow] = pos
    else:
        if cows[cow] != pos:
            cnt += 1
            cows[cow] = pos
print(cnt)