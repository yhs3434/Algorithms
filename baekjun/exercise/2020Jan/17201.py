# 자석 체인
# https://www.acmicpc.net/problem/17201
# https://github.com/yhs3434

n = int(input())
inp = input()
flag = False
for i in range(len(inp)-1):
    if inp[i] == inp[i+1]:
        flag = True
        break
if flag:
    print('No')
else:
    print('Yes')