# 약수
# https://www.acmicpc.net/problem/1037

n = int(input())
cd = list(map(int, input().split(' ')))
cd.sort()
print(cd[0]*cd[-1])