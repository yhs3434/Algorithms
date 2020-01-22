# 국영수
# https://www.acmicpc.net/problem/10825
# https://github.com/yhs3434

import sys
rl = sys.stdin.readline

n = int(input())
arr = []
for xxx in range(n):
    inp = rl().rstrip().split(' ')
    inp[1] = int(inp[1])
    inp[2] = int(inp[2])
    inp[3] = int(inp[3])
    arr.append(inp)

arr.sort(key = lambda key: key[0])
arr.sort(key = lambda key: key[3], reverse= True)
arr.sort(key = lambda key: key[2], reverse= False)
arr.sort(key = lambda key: key[1], reverse= True)
for a in arr:
    print(a[0])