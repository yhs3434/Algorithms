# 알파벳 개수
# https://www.acmicpc.net/problem/10808
# https://github.com/yhs3434/Algorithms

s = input()

cnts = [0] * 26

for c in s:
    cnts[ord(c)-ord('a')] += 1
for cnt in cnts:
    print(cnt, end=' ')