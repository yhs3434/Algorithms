# 수 정렬하기 4
# https://www.acmicpc.net/problem/11931

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)
for a in arr:
    print(a)