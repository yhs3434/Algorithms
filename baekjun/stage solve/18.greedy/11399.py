# ATM
# https://www.acmicpc.net/problem/11399

n = int(input())
ps = list(map(int, input().split(' ')))

ps.sort()
sumVal = 0
cnt = 0
for p in ps:
    cnt += p
    sumVal += cnt

print(sumVal)