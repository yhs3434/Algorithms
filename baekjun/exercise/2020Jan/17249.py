# 태보태보 총난타
# https://www.acmicpc.net/problem/17249

inp = input()
flag = False
cnt = [0, 0]
for i in range(len(inp)-4):
    cWin = inp[i:i+5]
    if cWin == '(^0^)':
        flag = True
    if not flag:
        if inp[i] == '@':
            cnt[0] += 1
    else:
        if inp[i+4] == '@':
            cnt[1] += 1
print(cnt[0], cnt[1])