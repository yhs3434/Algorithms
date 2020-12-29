N, M = map(int, input().split())

answer = ''
strN = str(N)
cnt = N

for i in range(M):
    j = i % len(strN)
    if j == 0:
        if i != 0:
            cnt -= 1
    if cnt == 0:
        break
    answer += strN[j]

print(answer)