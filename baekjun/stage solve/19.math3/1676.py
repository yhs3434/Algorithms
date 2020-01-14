# 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676

n = int(input())

cnt = n//5
cnt += (n//25)
cnt += (n//125)
print(cnt)