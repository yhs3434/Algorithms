# 차량 번호판 1
# https://www.acmicpc.net/problem/16968
# https://github.com/yhs3434/Algorithms

inp = input()
cur = 0
val = 0

if inp[0] == 'c':
    cur = 26
    val = 26
else:
    cur = 10
    val = 10

for i in range(1, len(inp)):
    if inp[i] == inp[i-1]:
        if inp[i] == 'c':
            cur = 25
        else:
            cur = 9
        val *= cur
    else:
        if inp[i] == 'c':
            cur = 26
            val *= cur
        else:
            cur = 10
            val *= cur
print(val)