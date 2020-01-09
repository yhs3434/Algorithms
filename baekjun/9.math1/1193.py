# 분수찾기
# https://www.acmicpc.net/problem/1193

def getSum(n):
    sumVal = 0
    for i in range(1, n+1):
        sumVal += i
    return sumVal

x = int(input())
if x==1:
    print('1/1')
else:
    stand = 0
    cnt = 1
    while x > stand:
        stand += cnt
        cnt += 1
    sp = True if cnt%2==1 else False
    cnt2 = x - getSum(cnt-2)
    if sp:
        i = 1
        j = cnt - i
        i += (cnt2-1)
        j -= (cnt2-1)
    else:
        j = 1
        i = cnt - j
        i -= (cnt2 - 1)
        j += (cnt2 - 1)
    print(str(i)+'/'+str(j))