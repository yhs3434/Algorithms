# 세탁소 사장 동혁
# https://www.acmicpc.net/problem/2720
# https://github.com/yhs3434/Algorithms

t = int(input())

for _ in range(t):
    num = int(input())
    answer = [0, 0, 0, 0]
    answer[0] += num//25
    num%=25
    answer[1] += num//10
    num%=10
    answer[2] += num//5
    num%=5
    answer[3] += num//1
    for a in answer:
        print(a, end=' ')
    print('')