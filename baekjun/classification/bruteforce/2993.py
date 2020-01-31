# 세 부분
# https://www.acmicpc.net/problem/2993
# https://github.com/yhs3434/Algorithms

inp = input()

from itertools import combinations

idxs = [i for i in range(1,len(inp))]
avails = list(combinations(idxs, 2))
arr = []

for avail in avails:
    i = avail[0]
    j = avail[1]

    word1 = inp[:i]
    word2 = inp[i:j]
    word3 = inp[j:]
    strr = word1[::-1] + word2[::-1] + word3[::-1]
    arr.append(strr)
arr.sort()
print(arr[0])
