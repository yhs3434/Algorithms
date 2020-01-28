# 수들의 합
# https://www.acmicpc.net/problem/1789
# https://jason9319.tistory.com/149

s = int(input())

num = 0
c = 0
cnt = 0
while num != s:
    c += 1
    num += c
    cnt += 1
    if num > s:
        cnt -= 1
        break
print(cnt)
