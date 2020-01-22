# Fridge of Your Dreams
# https://www.acmicpc.net/problem/11104
# https://github.com/yhs3434

n = int(input())
for xxx in range(n):
    inp = input()
    cnt = len(inp)-1
    answer = 0
    for c in inp:
        answer += (int(c)*(2**cnt))
        cnt -= 1
    print(answer)