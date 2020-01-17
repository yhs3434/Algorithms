# 0 = not cute / 1 = cute
# https://www.acmicpc.net/problem/10886

chash = {0:0, 1:0}
n = int(input())
for xxx in range(n):
    chash[int(input())] += 1
if chash[0] > chash[1]:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')