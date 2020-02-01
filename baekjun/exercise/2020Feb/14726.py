# 신용카드 판별
# https://www.acmicpc.net/problem/14726
# https://github.com/yhs3434/Algorithms

t = int(input())
for _ in range(t):
    inp = input()
    num = list(map(int, list(inp)))
    for i in range(len(num)):
        ii = len(num) - i - 1
        if i % 2 == 0:
            continue
        else:
            val = 2*num[ii]
            if val >= 10:
                val = val//10 + val%10
            num[ii] = val
    if sum(num) % 10 == 0:
        print('T')
    else:
        print('F')