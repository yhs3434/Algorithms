# ZOAC 2
# https://www.acmicpc.net/problem/18238
# https://github.com/yhs3434/Algorithms

inp = input()
cur = 'A'
answer = 0
for c in inp:
    val = 0
    if ord(c) > ord(cur):
        val = min(ord(c) - ord(cur), ord(cur) - (ord(c)-26))
    elif ord(c) < ord(cur):
        val = min(ord(cur) - ord(c), ord(c) - (ord(cur)-26))
    answer += val
    cur = c
print(answer)