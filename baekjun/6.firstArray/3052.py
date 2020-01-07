# 나머지
# https://www.acmicpc.net/problem/3052

sett = set()
for i in range(10):
    n = int(input())
    sett.add(n%42)
print(len(sett))