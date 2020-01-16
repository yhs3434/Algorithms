# 열 개씩 끊어 출력하기
# https://www.acmicpc.net/problem/11721

strr = input()
for i in range(len(strr)):
    if i%10 == 0 and i!=0:
        print('')
    print(strr[i], end='')