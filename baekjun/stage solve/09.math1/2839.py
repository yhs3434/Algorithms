# 설탕 배달
# https://www.acmicpc.net/problem/2839

n = int(input())

answer = 0

flag = True
for i in range(n//5, -1, -1):
    if n-5*i>=0 and (n-5*i)/3 == int((n-5*i)/3):
        answer += i
        answer += (n-5*i)//3
        flag = False
        break

if flag:
    answer = -1

print(answer)