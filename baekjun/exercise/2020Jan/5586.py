# JOI와 IOI
# https://www.acmicpc.net/problem/5586
# https://github.com/yhs3434

inp = input()

cnt = [0, 0]
for i in range(len(inp)-2):
    cur = inp[i:i+3]
    if cur == 'JOI':
        cnt[0] += 1
    elif cur == 'IOI':
        cnt[1] += 1
print(cnt[0])
print(cnt[1])