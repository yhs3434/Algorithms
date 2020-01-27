# 세로읽기
# https://www.acmicpc.net/problem/10798
# https://github.com/yhs3434/Algorithms

maxLen = 0
arr = []
for xxx in range(5):
    inp = input()
    arr.append(inp)
    if len(inp) > maxLen:
        maxLen = len(inp)
for j in range(maxLen):
    for i in range(5):
        if j < len(arr[i]):
            print(arr[i][j], end='')
