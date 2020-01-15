# 주차의 신
# https://www.acmicpc.net/problem/5054

t = int(input())
for xxx in range(t):
    n = int(input())
    stores = list(map(int, input().split(' ')))
    print(2*(max(stores)-min(stores)))