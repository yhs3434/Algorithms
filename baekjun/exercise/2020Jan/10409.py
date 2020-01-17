# 서버
# https://www.acmicpc.net/problem/10409

n, t = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
cnt = 0
for a in arr:
    t -= a
    if t >= 0:
        cnt += 1
    else:
        break
print(cnt)