# 한수
# https://www.acmicpc.net/problem/1065

def isHansu(num):
    if num < 100:
        return True
    nStr = str(num)
    flag = True
    for i in range(2, len(nStr)):
        if int(nStr[i-2]) - int(nStr[i-1]) != int(nStr[i-1]) - int(nStr[i]):
            flag = False
            break

    if flag:
        return True
    else:
        return False

N = int(input())
answer = 0

for n in range(1, N+1):
    if isHansu(n):
        answer += 1
print(answer)